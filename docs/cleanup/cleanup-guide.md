# Cleanup Guide

Run cleanup only after saving all screenshots and evidence.

Cleanup is destructive. Deleted resources may not be recoverable.

## 1. Manual Bedrock Cleanup

In the AWS Console, go to Amazon Bedrock in eu-west-2.

Check and delete, if no longer needed:

- Knowledge Base data source
- Knowledge Base
- Vector store or collection created for the Knowledge Base
- Guardrail
- Guardrail version, if created separately

Bedrock cleanup should be checked manually because some resources may not be removed by simple project scripts.

## 2. SSM Cleanup

Delete the project SSM Automation document if it exists.

Also delete the related IAM role after confirming it is not used by anything else.

## 3. Lambda Cleanup

Delete project Lambda functions with names starting with aiops-dev.

## 4. EventBridge Cleanup

Delete project EventBridge rules with names starting with aiops-dev.

## 5. SNS Cleanup

Delete the aiops-dev incident alert SNS topic.

## 6. CloudWatch Cleanup

Delete project CloudWatch alarms, dashboards, and log groups.

## 7. DynamoDB Cleanup

Delete the aiops-dev-incidents table if the project is complete.

## 8. S3 Cleanup

Empty and delete the project S3 bucket.

If the bucket has versioning enabled, delete current objects, previous versions, and delete markers before deleting the bucket.

## 9. IAM Cleanup

Delete project IAM roles and policies only after the related services have been removed.

If role deletion fails:

1. Detach managed policies.
2. Delete inline policies.
3. Remove trust relationships only if no longer needed.
4. Retry deleting the role.

## 10. Final Verification

Check these services in eu-west-2:

- Lambda
- CloudWatch
- EventBridge
- SNS
- DynamoDB
- S3
- Bedrock
- SSM
- IAM

Confirm no aiops-dev project resources remain unless you intentionally kept them.
