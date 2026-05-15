# Demo Script

## Project Name

AI CloudOps Incident Assistant

## 1. Introduction

This is a production-style AWS CloudOps portfolio project. It detects incidents from CloudWatch, processes them through event-driven services, stores audit history, sends alerts, and uses Amazon Bedrock with runbook RAG to generate safe incident triage guidance.

## 2. Business Problem

CloudOps teams often need to respond quickly to incidents. Manual triage can be slow, inconsistent, and dependent on engineer experience.

This project shows how AWS-native monitoring, event processing, and AI-assisted runbooks can improve triage speed while still keeping remediation controlled by human approval.

## 3. Architecture Walkthrough

The demo workload sends logs and metrics to CloudWatch.

A CloudWatch alarm detects an issue.

EventBridge routes the alarm event to the incident processor Lambda.

The incident processor stores records in DynamoDB, saves artifacts to S3, and sends an SNS email notification.

Runbooks are stored in S3 and indexed by Amazon Bedrock Knowledge Bases.

The AI analysis Lambda uses the incident record and runbook knowledge base to generate structured troubleshooting guidance.

Optional SSM Automation provides a human approval gate before remediation.

## 4. Demo Flow

1. Show the architecture diagram in the README.
2. Show the demo workload Lambda.
3. Trigger a controlled error.
4. Show the CloudWatch alarm.
5. Show the EventBridge rule.
6. Show the DynamoDB incident record.
7. Show the S3 artifact.
8. Show the SNS email alert.
9. Invoke the AI analysis Lambda.
10. Show the structured AI triage output.
11. Explain the Bedrock guardrail.
12. Show the SSM Automation approval gate.
13. Explain cleanup and cost control.

## 5. Key Production-Ready Points

- Event-driven design
- Audit history in DynamoDB and S3
- Human approval before remediation
- Guardrails for AI safety
- Least-privilege IAM approach
- Cleanup guide to avoid ongoing AWS costs

## 6. Closing Summary

This project demonstrates AWS CloudOps, incident response automation, AI-assisted triage, and safe production-style remediation design.
