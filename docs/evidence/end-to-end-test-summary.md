# End-to-End Test Evidence

Date: 2026-05-15 10:21:16
Project: AI CloudOps Incident Assistant
Environment: dev
Region: eu-west-2

Latest incident ID: inc-20260515091157-13d8195f
Alarm: aiops-dev-demo-workload-errors-critical
Demo workload Lambda: aiops-dev-demo-workload
AI analysis Lambda: aiops-dev-analysis-api

Expected result:
Alarm triggered, incident processed, DynamoDB/S3/SNS updated, and AI analysis generated.

Observed result:
The demo workload generated a controlled RuntimeError.
CloudWatch alarm entered ALARM state.
An incident ID was generated.
The AI analysis Lambda returned StatusCode 200.
The final AI analysis output was saved to docs/evidence/final-ai-analysis.json.

Evidence files:
- docs/evidence/test-end-to-end-error.json
- docs/evidence/final-ai-analysis.json
- docs/evidence/analysis-payload.json
- docs/evidence/force-error-payload.json
