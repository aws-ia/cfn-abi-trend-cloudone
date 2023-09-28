---
weight: 3
<<<<<<< before updating
title: Terminology
description: Terms used in this guide
---

* **ABI :** AWS Built-In (ABI).
* **ABI modules:** GitHub repositories based on AWS SRA, which provide templates for enabling AWS foundational services such as AWS CloudTrail, Amazon GuardDuty, AWS Security Hub, and other security services.
* **ABI projects:** The GitHub repositories built by partners in collaboration with AWS. While building these projects, partners use ABI modules to enable AWS services as needed before creating partner-specific assets. A project contains the following:
 * IaC templates to automate enablement of both AWS and partner services
 * Wrappers for common formats like CfCT manifest, SC baselines, and others to allow customers to pick and choose available services. For this package, we focus on including only the CfCT manifest file.
* **Trend Cloud One:** A platform built for cloud builders, where you can secure your cloud infrastructure.
* **Trend Vision One:** A platform that enhances and consolidates detection, investigation, and response capabilities across emails, endpoints, servers, cloud workloads, and networks.

**Next:** [Cost and licenses](/costandlicenses/index.html)
=======
title: Terminologies
description: Terminologies used in this guide.
---

* **ABI :**  AWS Built-In (ABI).
* **ABI modules :** The GitHub repositories based on AWS Security Reference Architecture (AWS SRA). The modules provide templates for enabling AWS foundational services such as AWS CloudTrail, Amazon GuardDuty, AWS Security Hub, etc.
* **ABI projects :** The GitHub repositories built by partners in collaboration with AWS. While building these projects, partners use ABI modules to enable AWS services as needed before creating partner-specific assets. The project contains (1) Infrastructure as Code (IaC) templates to automate enablement of both AWS and partner services, and (2) wrappers for most common formats such as CfCT manifest, AWS Service Catalog baselines, and more, so customers can pick and choose from the available services.
* **AWS Control Tower:** A service that helps you set up and govern a secure, multi-account AWS environment based on best practices.
* **AWS Organizations:** A service that helps you centrally manage and govern multiple AWS accounts.
* **IAM role:** An IAM entity that defines a set of permissions for making AWS service requests. Used to delegate access to AWS resources.
* **CloudFormation template:** A JSON- or YAML-formatted text file that describes the AWS resources and properties needed to run an application.
* **Stack:** A collection of AWS resources created and managed as a single unit when using AWS CloudFormation.
* **StackSet:** A CloudFormation resource type that helps you create, update, or delete stacks across multiple accounts and Regions with a single CloudFormation template.
* **IAM role ARN:** The Amazon Resource Name (ARN) that uniquely identifies an IAM role in AWS.
* **External ID:** An identifier that helps ensure that the intended AWS role is used for cross-account access.

* [[Add more terminologies here]]
* //REMOVE UNWANTED TERMINOLOGIES //

**Next:** See [Cost and licenses](/costandlicenses/index.html) to get started.
>>>>>>> after updating
