# Bedrock Knowledge Base IDs

Knowledge base name: aiops-dev-runbook-kb
Knowledge base ID: <resource-id>

Data source name: aiops-dev-runbook-kb
Data source type: Amazon S3
S3 runbook bucket: <bucket-name>
S3 runbook prefix: runbooks/

Embedding model: amazon.titan-embed-text-v2:0
Embedding model display name: Titan Text Embeddings v2
Vector dimensions: 1024

Vector store: Amazon S3 Vectors
AWS Region: eu-west-2

Console retrieval test status: Successful
Test query: How should I triage a Lambda error spike?
Expected retrieved content: Lambda Error Spike runbook, Incident Communication runbook, CloudWatch Alarm Investigation runbook, and AI Assistant Safety Rules.
