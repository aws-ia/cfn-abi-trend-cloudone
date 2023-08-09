---
weight: 12
title: Troubleshooting
description: Troubleshooting
---

## Common ABI issues

For troubleshooting common ABI issues, refer to the [AWS Built-In General Information Guide](http://link-to-reference-architecture) and [Troubleshooting CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html).

## SSM integration

### No green indicator

1. Log in to your AWS account.
2. Navigate to **Systems Manager** > **Parameter Store**, and confirm that the four created parameters exist.
3. Navigate to **Systems Manager** > **State Manager**.
4. For agent association details, choose **Association ID** > **Execution History** > **Failed execution**.

**Next:** [Feedback](/feedback/index.html)
