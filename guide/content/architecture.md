---
weight: 5
title: Architecture
description: Solution architecture
---

Deploying this ABI package with default parameters builds the following architectures.

##### AWS CloudTrail integration architecture diagram

![AWS CloudTrail integration architecture diagram](/images/cloudtrail-architecture.png)

As shown in the diagram, this integration sets up the following:

* In the log archive account:
  * Amazon CloudWatch events rules to detect new PUTs in the organizational CloudTrail S3 bucket and trigger an AWS Lambda function.
  * The Lambda function forwards the new CloudTrail events to Trend Vision One.

##### SSM integration architecture diagram

![SSM integration architecture diagram](/images/ssm-architecture.jpg)

* In each AWS Organizations account:
  * Four system-manager parameters are created in each AWS Region.
  * For a defined CRON job, the AWS Systems Manager workload security agent association package triggers for '*' instances managed by SSM.
  * The SSM association package deploys workload security agent for unmanaged instances.

##### AWS Security Hub integration architecture diagram

To do.

<!--
![SecurityHub Integration Architecture Diagram](/images/)

As shown in the diagram, this integration sets up the following:

* In all current and AWS accounts in your AWS organization:
    * <Amazon CloudWatch Events rules> to <detect changes in AWS Config configuration items (CIs)> and <trigger AWS Lambda functions>.
    * <Service> to perform <Action-1> and <Action-2>.

* In the management account:
    * <Service> to perform <Action-1> and <Action-2>.

* In the log archive account:
    * <Service> to perform <Action-1> and <Action-2>.

* In the security tooling account:
    * <Service> to perform <Action-1> and <Action-2>.

-->

**Next:** [Deployment Options](/deployment-options/index.html)
