# Runbook: Incident Communication

## Purpose
Provide a consistent communication format during operational incidents.

## Severity model
Critical: user-facing outage, repeated failures, security risk, or data-loss risk.
High: degraded service with workaround.
Medium: limited impact.
Low: informational issue.

## Communication template
Incident summary:
Current status:
Known impact:
Actions taken:
Next update:

## Safe communication rules
- Do not speculate.
- Clearly state what is confirmed and what is still being investigated.
- Avoid exposing internal AWS account details.
- Do not include secrets, tokens, or customer data.

## Evidence to capture
- Incident timeline.
- Alarm screenshots.
- Log screenshots.
- Actions taken and approval notes.

## Escalation
Escalate Critical and High incidents to the responsible engineer or incident owner.
