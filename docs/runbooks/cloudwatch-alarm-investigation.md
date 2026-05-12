# Runbook: CloudWatch Alarm Investigation

## Purpose
Investigate CloudWatch alarms for the AI CloudOps Incident Assistant project.

## Symptoms
- A CloudWatch alarm changes to ALARM state.
- Metrics show unusual errors, throttles, latency, or failed invocations.
- Logs show application or runtime exceptions.

## Initial triage
1. Confirm the alarm name and current state.
2. Record the alarm timestamp.
3. Review the metric graph for the affected resource.
4. Review logs for the same time window.
5. Compare recent deployments or configuration changes.
6. Capture evidence before remediation.
7. Document root cause and follow-up actions.

## Safe remediation
- Prefer reversible changes.
- Do not delete resources during investigation.
- Do not modify IAM policies unless access failure is confirmed.
- Get manual approval before any automated remediation.

## Evidence to capture
- Alarm screenshot.
- Metric graph screenshot.
- Related CloudWatch log entries.
- Any recent configuration or deployment change.

## Escalation
Escalate if the alarm remains active, the root cause is unclear, or customer-facing impact is suspected.
