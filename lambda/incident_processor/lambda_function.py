import json
import os
import boto3
from datetime import datetime, timezone

sns = boto3.client("sns")
dynamodb = boto3.resource("dynamodb")
s3 = boto3.client("s3")


def lambda_handler(event, context):
    now = datetime.now(timezone.utc)
    incident_id = f"inc-{now.strftime('%Y%m%d%H%M%S')}-{context.aws_request_id[:8]}"

    detail = event.get("detail", {})
    state = detail.get("state", {})

    normalized = {
        "incident_id": incident_id,
        "alarm_name": detail.get("alarmName", "unknown-alarm"),
        "state": state.get("value", "UNKNOWN"),
        "reason": state.get("reason", "No reason provided"),
        "source": event.get("source"),
        "detail_type": event.get("detail-type"),
        "created_at": now.isoformat(),
        "severity": "critical",
    }

    print(json.dumps({"normalized_incident": normalized, "raw_event": event}, default=str))

    table_name = os.environ["INCIDENT_TABLE_NAME"]
    bucket_name = os.environ["INCIDENT_BUCKET_NAME"]
    topic_arn = os.environ.get("SNS_TOPIC_ARN")

    table = dynamodb.Table(table_name)
    table.put_item(Item=normalized)

    s3_key = f"incidents/{incident_id}.json"

    s3.put_object(
        Bucket=bucket_name,
        Key=s3_key,
        Body=json.dumps(
            {
                "incident": normalized,
                "raw_event": event
            },
            indent=2,
            default=str
        ).encode("utf-8"),
        ContentType="application/json",
    )

    if topic_arn:
        sns.publish(
            TopicArn=topic_arn,
            Subject=f"AI CloudOps Incident: {normalized['alarm_name']} is {normalized['state']}",
            Message=json.dumps(
                {
                    "incident": normalized,
                    "s3_artifact": f"s3://{bucket_name}/{s3_key}"
                },
                indent=2
            ),
        )

    return {
        "statusCode": 200,
        "incident_id": incident_id,
        "s3_key": s3_key
    }
