# AI CloudOps Incident Assistant

Production-ready portfolio project using AWS CloudWatch, EventBridge, Lambda, SNS, DynamoDB, S3, Amazon Bedrock, Bedrock Knowledge Bases, Guardrails, and SSM Automation.

## Production Hardening Notes

This project is a production-style CloudOps Incident Assistant designed to demonstrate incident detection, event-driven automation, AI-assisted triage, RAG over operational runbooks, Bedrock Guardrails, audit logging, and human-approved remediation.

The project is not intended to run unattended in a real production AWS account without additional controls.

Implemented hardening controls include:

- Least-privilege IAM review
- CloudWatch log retention set to 7 days for demo Lambda log groups
- SNS-based incident notification
- DynamoDB-based incident storage
- S3-based incident evidence storage
- Project resource tagging for ownership and cost tracking
- Bedrock Guardrails
- Human approval before remediation
- Cost-conscious cleanup planning

Future production improvements:

- Add API Gateway authentication using IAM, JWT, or Cognito
- Add Lambda dead-letter queues or Lambda destinations
- Add stronger CI/CD with Terraform or AWS CDK
- Add automated security scanning
- Add multi-environment deployment such as dev, staging, and production
- Add more detailed audit and compliance reporting
