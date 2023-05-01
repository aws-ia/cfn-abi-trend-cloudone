# AWS Organizations Trend Cloud One Workload Security SSM Automation
---

Distributor is a feature integrated with AWS Systems Manager that you can use to securely store and distribute software packages in your accounts. 
By integrating Workload Security with AWS Systems Manager Distributor, you can distribute Cloud One Workload Security agents across multiple platforms, control access to managed instances, and automate your deployments.

This solution will distribute Workload Security across OU member accounts across all default enabled regions.

## What this solution does.

1. This stack is deployed in the Organizational management account as a CloudFormation template.
2. On deployment, a StackSet will be created in every AWS Account from the provide OU-IDs.
3. Four parameters will be created in AWS Systems Manager Parameter Store in each region.
4. A Systems Manager Association will run on creation that will deploy the Workload Security Agent on every['*'] instance.
5. A CRON Job is also created to run subsequent associations on a schedule.

---

![architecture](org-img.jpg)

---

## Requirements

1. There are 4 parameters that need to be copied. On the Workload Security console, **go to Support > Deployment Scripts**.
  - **dsActivationUrl** -	Go to the top of the generated script and copy the dsActivationUrl.
  - **dsManagerUrl** - Go to the top of the generated script and copy the dsManagerUrl.
  - **dsTenantId** - Scroll to the bottom of the generated script and copy the tenantID.
  - **dsToken** - Scroll to the bottom of the generated script and copy the token.

2. Download the Yaml Template named ```c1ws-ssm-orgs.template.yaml```.

---

## How to Deploy

To deploy the solution, launch this CloudFormation template in your organization’s management account.

1. Provide the following inputs for the template parameters:

#### [AccountAdminStatus]
  - Stack Name: Enter a name for the Stack.
  - AccountAdminStatus: Specify if the solution will use a delegated administrator account within the Organization to manage the software packages. CloudFormation StackSet IAM roles should be provisioned beforehand.

#### [Targets]
  - DeploymentTargets: Specify AWS account IDs and/or the organizational unit IDs within AWS Organization whose accounts have the target instances (e.g., ou-name, 123456789123) for distribution
  - TargetKey: Specify which instances have to be targeted for this solution. Allowed values – ParameterValues, ResourceGroup or begin with tag:, AWS::EC2::Instance, InstanceIds (default), instanceids. Refer to Target for more details.
  - TargetValues: Specify the target key values specified above. Default is *.
  - CronJob: Specify the CRON Job for future scheduling. 
    - [Default is everyday @10:15AM - cron(15 10 * * ? *)] [see here](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html)
#### [Cloud One Workload Security]
These were copied down from the worklaod security deployment script.
  - dsActivationUrl
  - dsManagerUrl 	
  - dsTenantId
  - dsToken

2. Launch the Stack.

---

## Limitations
---
1. EC2 instances must have the SSM agent installed. Click the link for [supported SSM OS platforms](https://docs.aws.amazon.com/systems-manager/latest/userguide/prereqs-operating-systems.html).
2. EC2 instances must have the required SSM permissions. Click the link for [setup configuration](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html).
3. StackSets doesn't deploy stack instances to the organization management account, even if the organization management account is in your organization or in an OU in your organization. See here for [DeploymentTargets](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html).


---


