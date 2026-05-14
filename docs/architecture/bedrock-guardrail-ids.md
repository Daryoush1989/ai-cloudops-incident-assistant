# Bedrock Guardrail Configuration

Project: AI CloudOps Incident Assistant
Environment: dev
AWS Region: eu-west-2

Guardrail name: aiops-dev-incident-assistant-guardrail
Guardrail ID: rx2j6rbme0lg
Guardrail version: 2
Guardrail ARN: arn:aws:bedrock:eu-west-2:969566116923:guardrail/rx2j6rbme0lg

Purpose:
Safety controls for AI CloudOps incident analysis.

Important note:
Create a guardrail version after saving the working draft. Do not use DRAFT for production-style application configuration. The Bedrock API/application should reference the Guardrail ID plus the concrete version number.

Safety goals:
- Block credential exposure requests.
- Block security bypass requests.
- Block unsafe destructive remediation as a first response.
- Mask or block sensitive information.
- Require evidence before root cause attribution.
- Encourage investigation, approval, rollback planning, and runbook-based remediation.
