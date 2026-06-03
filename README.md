# AI CloudOps Incident Assistant

## Overview

AI CloudOps Incident Assistant is an AWS CloudOps portfolio project that demonstrates event-driven incident detection, incident record storage, notification workflows, runbook-grounded AI analysis, and human-approved remediation planning.

The repository includes Lambda functions, IAM policy examples, EventBridge and CloudWatch configuration examples, Bedrock Knowledge Base and Guardrail documentation, operational runbooks, test payloads, and sanitized documentation evidence.

## Business Problem

Cloud operations teams need a repeatable way to detect incidents, collect context, notify responders, and produce safe triage guidance. Manual triage can be slow, inconsistent, and risky when remediation is attempted without evidence or approval.

This project demonstrates how AWS services can support an incident workflow that keeps automation helpful while preserving human approval for remediation.

## Architecture

High-level flow:

```text
Demo workload
  -> CloudWatch Logs and metrics
  -> CloudWatch Alarm
  -> EventBridge rule
  -> Incident Processor Lambda
  -> DynamoDB incident table
  -> S3 incident artifact
  -> SNS notification
  -> AI Analysis Lambda
  -> Bedrock Knowledge Base and Guardrails
  -> Structured triage guidance
  -> Optional SSM Automation with human approval
```

## AWS Services Used

- AWS Lambda
- Amazon CloudWatch
- Amazon EventBridge
- Amazon DynamoDB
- Amazon S3
- Amazon SNS
- Amazon Bedrock
- Bedrock Knowledge Bases
- Bedrock Guardrails
- AWS Systems Manager Automation
- AWS IAM

## Tools Used

- Python
- JSON policy and test payloads
- Markdown operational runbooks
- CloudWatch dashboard configuration
- Git and GitHub

## Security Features

- Incident guidance is grounded in runbooks instead of free-form remediation.
- Bedrock Guardrails are documented for safer AI output.
- SSM Automation is designed around human approval.
- IAM policy examples are scoped to the required incident resources.
- Evidence collection is separated from credentials and secrets.
- Remediation guidance warns against destructive changes without proof.

## Deployment Summary

The repository documents a lab-style CloudOps incident workflow using AWS managed services. It includes Lambda handlers for the demo workload, incident processing, and AI analysis. Infrastructure support files exist in the repository but should be sanitized before public release.

No AWS deployment or cleanup commands were run during this README refresh.

## Testing and Validation

Validation evidence includes:

- Healthy and error workload payloads
- CloudWatch alarm evidence
- Incident record payloads
- AI analysis request and response examples
- End-to-end incident test summary
- Guardrail and runbook safety documentation

## Evidence / Screenshots

Sanitized documentation evidence is stored under `docs/evidence`. Raw lab evidence under the top-level `evidence/` folder and infrastructure support files should be reviewed before public release because they may contain account-specific ARNs, bucket names, CloudWatch resources, or resource IDs. Before using those files publicly, redact values with placeholders such as `<aws-account-id>`, `<bucket-name>`, `<alarm-name>`, `<lambda-name>`, and `<resource-id>`.

## Cost Control

The project includes cleanup documentation and uses services that should be removed or retained carefully after testing, including Lambda functions, DynamoDB tables, S3 buckets, CloudWatch log groups, SNS topics, Bedrock resources, and SSM automation documents.

## Cleanup

Follow the cleanup documentation under `docs/cleanup` after evidence capture. Confirm that test alarms, log groups, S3 artifacts, DynamoDB records, Bedrock resources, SNS topics, and IAM roles are removed or intentionally retained.

## Lessons Learned

- CloudOps incident workflows need detection, storage, notification, analysis, and approval controls.
- AI can help summarize incidents, but it should not perform unsupervised remediation.
- Runbooks improve consistency and reduce unsafe assumptions during triage.
- Evidence files are valuable for recruiters, but they must be sanitized before publication.

## Future Improvements

- Redact account IDs, ARNs, bucket names, and resource IDs from raw evidence and infrastructure support files.
- Keep only sanitized screenshots in public documentation.
- Add Terraform or CDK for repeatable infrastructure deployment.
- Add automated tests for Lambda handlers and prompt safety behavior.
- Add a sanitized architecture diagram for public portfolio use.
