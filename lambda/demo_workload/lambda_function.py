import json
import os
import time


def lambda_handler(event, context):
    """Demo workload for the AI CloudOps Incident Assistant."""
    force_error = bool(event.get("force_error")) or os.getenv("FORCE_ERROR", "false").lower() == "true"

    log_event = {
        "service": "demo-workload",
        "request_id": context.aws_request_id,
        "force_error": force_error,
        "timestamp": int(time.time()),
    }
    print(json.dumps(log_event))

    if force_error:
        raise RuntimeError("Simulated production incident: demo workload forced error")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Demo workload healthy",
            "request_id": context.aws_request_id
        }),
    }
