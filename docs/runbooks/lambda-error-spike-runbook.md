# Runbook: Lambda Error Spike

## Purpose
Triage and remediate Lambda error spikes for the AI CloudOps demo workload.

## Symptoms
- CloudWatch alarm aiops-dev-demo-workload-errors-critical enters ALARM.
- Lambda Errors metric is >= 1 within 60 seconds.
- CloudWatch logs show RuntimeError or application exceptions.

## Initial triage
1. Confirm the alarm name and state in CloudWatch.
2. Open the Lambda log group /aws/lambda/aiops-dev-demo-workload.
3. Review the latest log stream and identify the request ID.
4. Check if errors were caused by a controlled test event with force_error=true.
5. Confirm whether FORCE_ERROR environment variable is true.

## Safe remediation
- If FORCE_ERROR is true, set it back to false.
- Do not delete the Lambda function during an incident.
- Do not change IAM permissions unless the root cause is proven.
- Any automated remediation must require manual approval.

## Evidence to capture
- Screenshot of the CloudWatch alarm state.
- Screenshot of the Lambda log group.
- Relevant request ID from the failed invocation.
- Any configuration change made during remediation.

## Escalation
Escalate if errors continue after FORCE_ERROR=false or if logs show unknown application exceptions.
