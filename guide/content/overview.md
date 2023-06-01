---
weight: 2
title: Overview
description: 
---


This ABI deploys Trend Micro Integrations for AWS Organizations on the AWS Cloud. It’s for Cloud Operations, SecOps, Cloud Builders and anyone else that want to provide security across multiple AWS accounts. If you are unfamiliar with AWS Built In, refer to the [AWS Built in](https://aws.amazon.com/builtin).

Deploying this ABI package does not guarantee an organization’s compliance with any laws, certifications, policies, or other regulations.

## Security Outcomes

The Trend Micro AWS Built In module can be use to help you achieve up to three different security outcomes across your organization:

### CloudTrail Analyzes

The XDR capability of Trend Micro Vision One applies effective expert analytics and global threat intelligence using data collected across multiple vectors - email, endpoints, servers, cloud workloads, and networks. Trend Micro Vision One can also analyze the AWS CloudTrail logs from your AWS Accounts, identify threats and attacks, alert you to problems, and create a visualization of the log.

This ABI module integrates your organizational trail with Trend Vision One, making sure all CloudTrail events across all accounts in your organization are being analyzed by Vision One.

### EC2 Instance security agent deployment via SSM

Distributor is a feature integrated with AWS Systems Manager that you can use to securely store and distribute software packages in your accounts. By integrating Workload Security with AWS Systems Manager Distributor, you can distribute Cloud One Workload Security agents across multiple platforms, control access to managed instances, and automate your deployments.

This ABI module is deployed across selected or all accounts and regions and makes sure the Trend Cloud One Workload Security agent is deployed to the targeted EC2 instances.

### SecurityHub Integration

Security Hub collects security data from across AWS accounts, services, and supported third-party partner products and helps you analyze your security trends and identify the highest priority security issues. By integrating the Trend Cloud One, you can leverage the consolidates of your security findings of your containers inside SecurityHub.

This ABI module makes sure all your Trend Cloud events for supported modules are visible in your main Security Hub account/region.

## AWS Marketplace listings

* [Trend Cloud One](https://aws.amazon.com/marketplace/pp/prodview-g232pyu6l55l4)
* [Trend Vision One](https://aws.amazon.com/marketplace/pp/prodview-jktqkevcm3zbc)

**Next:** Choose [Terminologies](/terminologies/index.html) to get started.
