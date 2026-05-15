# Production Readiness Checklist

## Security
- [x] IAM roles are least privilege.
- [x] No secrets in code or Git.
- [x] S3 public access is blocked.
- [x] Bedrock Guardrails configured.
- [x] Remediation requires human approval.
- [ ] API endpoint authentication is planned as a future improvement.
- [x] Wildcard IAM permissions are avoided unless required by the AWS service.

## Observability
- [x] CloudWatch alarms configured.
- [x] Log retention set to 7 days for demo Lambda log groups.
- [x] CloudWatch dashboard exists.
- [x] Incident processor logs normalized events.
- [x] Lambda errors can be investigated through CloudWatch Logs.

## Reliability
- [x] Event-driven flow tested.
- [x] Incident storage tested.
- [x] SNS notification tested.
- [x] AI analysis tested.
- [x] Repeated alarm events are considered.
- [ ] Future improvement: add Lambda dead-letter queue or Lambda destinations.

## AI Safety and Governance
- [x] Bedrock Guardrails configured.
- [x] Runbook-grounded responses tested.
- [x] Human approval required before remediation.
- [x] AI output is treated as advisory, not fully autonomous.

## Cost control
- [x] Minimal resources created.
- [x] Cleanup guide reviewed.
- [x] Bedrock Knowledge Base/vector store deletion steps documented.
- [x] Log retention configured to avoid indefinite CloudWatch log storage.
- [x] Project resources tagged for ownership and cost tracking.
- [ ] Final cleanup step planned.
