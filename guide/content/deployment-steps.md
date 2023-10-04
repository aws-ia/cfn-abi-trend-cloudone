---
weight: 8
title: Deployment steps
description: Deployment steps
---

## Launch the CloudFormation template in the AWS Organizations management account {#launch-cfn}

1. Download the [CloudFormation template](https://a.co/aMaMlJd) to your local machine.
2. Launch the CloudFormation template in your AWS Control Tower home Region.
    * Stack name: `template-trend-micro-enable-integrations`
    * List parameters with [call out default values and update below example as needed]
      * Mandatory parameters
        * **CloudOneApiKey**: Your Cloud One API Key. For more information, refer to [Manage API keys](https://cloudone.trendmicro.com/docs/identity-and-account-management/c1-api-key/)
        * **OrganizationId**: Your AWS Organization ID. For more information, refer to [Viewing details about your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_details.html).
      * Parameters for the ABI module:
        * **DeployCloudTrailIntegration**: `true`
        * **DeploySSMIntegration**: `true`
        * **DeploySecurityHubIntegration**: `true`
      * Parameters related to the CloudTrail integration:
        * **VisionOneAuthenticationToken**: Vision One authentication token. For more information, refer to [Obtaining API Keys for Third-Party Apps](https://docs.trendmicro.com/en-us/enterprise/trend-vision-one-olh/administrative-setti/user-accounts/obtaining-api-keys-f_001.aspx).
        * **VisionOneRegion**: Vision One Region. For more information, refer to [Regional Domains](https://automation.trendmicro.com/xdr/Guides/Regional-Domains).
        * **ExistingOrganizationalCloudtrailBucketName**: Bucket name of an existing organizational CloudTrail. For more information, refer to [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html).
      * Parameters related to the SSM integration:
        * **CronJob**: `cron(15 10 * * ? *)`
        * **AccountAdminStatus**: `SELF`
      * Parameters related to the Security Hub integration:
        * **EnableSecurityHub**: Set to `false` unless you don't have Security Hub enabled. Set to `true` to enable Security Hub in the audit account.

3. Choose both the **Capabilities** and then **Submit** to launch the stack.

    [] I acknowledge that AWS CloudFormation might create IAM resources with custom names.

    [] I acknowledge that AWS CloudFormation might require the following capability: CAPABILITY_AUTO_EXPAND

Wait for the CloudFormation status to change to `CREATE_COMPLETE`.

## Launch using Customizations for Control Tower {#launch-cfct}

[CfCT](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/) combines AWS Control Tower and other highly available, trusted AWS services to help customers more quickly set up a secure, multiaccount AWS environment according to AWS best practices. You can add customizations to your AWS Control Tower landing zone using an AWS CloudFormation template and service control policies (SCPs). You can deploy the custom template and policies to individual accounts and organizational units within your organization.

CfCT also integrates with AWS Control Tower lifecycle events to help ensure that resource deployments stay in sync with your landing zone. For example, when a new account is created using the AWS Control Tower account factory, CfCt helps to ensure that all resources attached to the account's organizational unit are automatically deployed.

The templates provided as part of the ABI packages are deployable using CfCT. For more information, refer to [Prerequisites](/prerequisites.html).

### Prerequisites

1. For CfCT to launch resources from the management account, you must create a role with necessary permissions in that account.

### How it works

To deploy this integration page using CfCT, add the following blurb to the `manifest.yaml` file, and update the accounts and organizational units as needed.

```yaml
resources:
  - name: sra-enable-partner1-solution
    resource_file: https://aws-abi.s3.us-east-1.amazonaws.com/cfn-abi-trend-cloudone/templates/main.template.yaml
    deploy_method: stack_set
    parameters:
      - parameter_key: pProductArn
        parameter_value: arn:aws:securityhub:us-east-1::product/cloud-custodian/cloud-custodian
      - parameter_key: pSRASourceS3BucketName
        parameter_value: aws-abi
      - parameter_key: pSRAStagingS3KeyPrefix
        parameter_value: cfn-abi-aws-reference-guide
      - parameter_key: CloudOneApiKey
        parameter_value: Your Cloud One API key. For more information, refer to [Manage API keys](https://cloudone.trendmicro.com/docs/identity-and-account-management/c1-api-key/).
      - parameter_key: OrganizationId
        parameter_value: Your AWS Organization ID. For more information, refer to [Viewing details about your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_details.html).
      - parameter_key: DeployCloudTrailIntegration
        parameter_value: true
      - parameter_key: DeploySSMIntegration
        parameter_value: true
      - parameter_key: DeploySecurityHubIntegration
        parameter_value: true
      - parameter_key: VisionOneAuthenticationToken
        parameter_value: Vision One authentication token. For more information, refer to [Obtaining API Keys for Third-Party Apps](https://docs.trendmicro.com/en-us/enterprise/trend-vision-one-olh/administrative-setti/user-accounts/obtaining-api-keys-f_001.aspx).
      - parameter_key: VisionOneRegion
        parameter_value: Vision One Region. For more information, refer to [Regional Domains](https://automation.trendmicro.com/xdr/Guides/Regional-Domains).
      - parameter_key: ExistingOrganizationalCloudtrailBucketName
        parameter_value: Bucket name of an existing Organizational CloudTrail. For more information, refer to [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html).
      - parameter_key: CronJob
        parameter_value: cron(15 10 * * ? *)
      - parameter_key: AccountAdminStatus
        parameter_value: SELF
      - parameter_key: EnableSecurityHub
        parameter_value: false
    deployment_targets:
      accounts:
        - [[MANAGEMENT-AWS-ACCOUNT-ID]]
```

**Next:** [Postdeployment options](/post-deployment-steps/index.html)
