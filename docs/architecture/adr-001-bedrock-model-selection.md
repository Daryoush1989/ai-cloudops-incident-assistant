# Architecture Decision Record: AI model selection

Date: 2026-05-12
Region: eu-west-2
Text model selected: amazon.nova-lite-v1:0
Embedding model selected: amazon.titan-embed-text-v2:0
Reason: Use Bedrock for incident summarization, triage, and runbook-grounded recommendations.
Fallback: If a required model is not available in eu-west-2, document the alternate Bedrock region and keep the rest of the project in eu-west-2.
