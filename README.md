# AI CloudOps Incident Assistant

## Overview

Production-style AWS portfolio project that detects CloudWatch incidents, processes alarm events, stores audit history, sends notifications, and uses Amazon Bedrock with runbook RAG to generate safe incident triage guidance.

This project demonstrates modern CloudOps, incident response, event-driven automation, and safe AI-assisted troubleshooting.

## Architecture

~~~mermaid
flowchart TD
    A[Demo Lambda Workload] --> B[CloudWatch Logs and Metrics]
    B --> C[CloudWatch Alarm]
    C --> D[EventBridge Rule]
    D --> E[Incident Processor Lambda]
    E --> F[DynamoDB Incident Table]
    E --> G[S3 Incident Artifacts]
    E --> H[SNS Email Alert]
    I[S3 Runbooks] --> J[Bedrock Knowledge Base]
    F --> K[AI Analysis Lambda]
    J --> K
    K --> L[Bedrock Model and Guardrails]
    K --> M[Structured Triage Output]
    M --> N[Optional SSM Automation with Human Approval]
~~~

## Services Used

- AWS Lambda
- Amazon CloudWatch
- Amazon EventBridge
- Amazon SNS
- Amazon DynamoDB
- Amazon S3
- Amazon Bedrock
- Bedrock Knowledge Bases
- Bedrock Guardrails
- AWS Systems Manager Automation
- IAM

## Production-Ready Features

- Event-driven incident detection
- CloudWatch alarm-based incident trigger
- EventBridge routing
- Incident audit storage in DynamoDB
- Incident artifacts stored in S3
- SNS email alerting
- Runbook-grounded AI analysis using Bedrock Knowledge Bases
- Guardrails for safer AI output
- Human-approved remediation using SSM Automation
- Least-privilege IAM design
- Log retention and cleanup planning
- Evidence-based portfolio documentation

## Demo Flow

1. Invoke the demo workload with force_error=true.
2. CloudWatch Logs and metrics capture the error.
3. CloudWatch alarm enters ALARM state.
4. EventBridge invokes the incident processor Lambda.
5. Incident details are stored in DynamoDB.
6. Incident artifact is saved to S3.
7. SNS sends an email notification.
8. AI analysis Lambda uses Bedrock and the runbook knowledge base.
9. Structured triage guidance is generated.
10. Optional SSM Automation waits for human approval before remediation.

## Repository Structure

~~~text
ai-cloudops-incident-assistant/
├── README.md
├── docs/
│   ├── demo-script.md
│   ├── cleanup/
│   │   └── cleanup-guide.md
│   └── evidence/
├── runbooks/
├── src/
└── tests/
~~~

## Evidence

Save screenshots in docs/evidence/.

Recommended evidence:

- Final GitHub README
- Architecture diagram rendered in GitHub
- CloudWatch alarm
- EventBridge rule
- Lambda functions
- DynamoDB incident record
- S3 incident artifact
- SNS email alert
- Bedrock Knowledge Base
- Bedrock Guardrail
- SSM Automation approval step

## Cleanup

Follow docs/cleanup/cleanup-guide.md when the project is complete.

Do not run cleanup until all evidence has been captured.
