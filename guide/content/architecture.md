---
weight: 5
title: Architecture
description: Solution architecture.
---

Deploying this ABI package with default parameters builds the following architectures.

##### CloudTrail Integration Architecture Diagram

![CloudTrail Integration Architecture Diagram](/images/cloudtrail-architecture.png)

As shown in the diagram, this integration sets up the following:

* In the log archive account:
  * Amazon CloudWatch Events rules to detect new PUTs in the Organizational CloudTrail S3 Bucket and trigger a AWS Lambda function
  * This function forwards the new CloudTrail events to Trend Vision One

##### SSM Integration Architecture Diagram

![SSM Integration Architecture Diagram](/images/ssm-architecture.jpg)

* In each AWS Organizational OU's accounts:
  * Four System Manager Parameters are created in each AWS Region.
  * On defined CRON Job, AWS Systems Manager Workload Security Agent Association Package will be trigger for '*' Instances managed by SSM.
  * This SSM Association package will deploy Workload Security Agent on unmanaged Instances

##### SecurityHub Integration Architecture Diagram

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

**Next:** Choose [Deployment Options](/deployment-options/index.html) to get started.
