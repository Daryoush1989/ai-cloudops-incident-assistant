import json
import os
import boto3
from decimal import Decimal

bedrock_agent_runtime = boto3.client("bedrock-agent-runtime")
dynamodb = boto3.resource("dynamodb")


def _json_default(value):
    if isinstance(value, Decimal):
        return int(value) if value % 1 == 0 else float(value)
    raise TypeError


def lambda_handler(event, context):
    table_name = os.environ["INCIDENT_TABLE_NAME"]
    knowledge_base_id = os.environ["KNOWLEDGE_BASE_ID"]
    model_arn = os.environ["BEDROCK_MODEL_ARN"]

    body = event.get("body")

    if isinstance(body, str):
        body = json.loads(body or "{}")
    elif body is None:
        body = event

    incident_id = body.get("incident_id")

    if not incident_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "incident_id is required"})
        }

    table = dynamodb.Table(table_name)

    item = table.get_item(
        Key={"incident_id": incident_id}
    ).get("Item")

    if not item:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "incident not found"})
        }

    prompt = f"""
You are an AI CloudOps Incident Assistant.

Analyze this incident using the retrieved runbook context.

Incident:
{json.dumps(item, default=_json_default, indent=2)}

Return JSON with:
- summary
- likely_root_causes
- immediate_triage_steps
- safe_remediation_options
- evidence_to_collect
- escalation_needed

Rules:
- Do not invent logs or metrics.
- State uncertainty clearly.
- Do not recommend destructive actions.
- Any remediation must require human approval.
"""

    response = bedrock_agent_runtime.retrieve_and_generate(
        input={"text": prompt},
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": knowledge_base_id,
                "modelArn": model_arn
            }
        }
    )

    output_text = response.get("output", {}).get("text", "")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(
            {
                "incident_id": incident_id,
                "analysis": output_text
            },
            default=_json_default
        )
    }
