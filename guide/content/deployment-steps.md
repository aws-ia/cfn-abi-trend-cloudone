---
weight: 8
title: Deployment steps
description: Deployment steps
---

## Launch the CloudFormation Template in the Management Account

1. Download the cloudformation template from source: https://aws-abi-pilot.s3.us-east-1.amazonaws.com/cfn-abi-trend-cloudone/main/templates/main.template.yaml
2. Launch CloudFormation template in your AWS Control Tower home region.
    * Stack name: `template-trend-micro-enable-integrations`
    * List Parameters with [call out default values and update below example as needed]
      * Mandatory Parameters
        * **CloudOneApiKey**: Your Cloud One API Key. You can learn more about it [here](https://cloudone.trendmicro.com/docs/identity-and-account-management/c1-api-key/)
        * **OrganizationId**: Your AWS Organization Id. You can learn how to find yours following [this](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_details.html) AWS documentation.
      * Parameters to select which modules of this ABI you'd like to deploy:
        * **DeployCloudTrailIntegration**: `true`
        * **DeploySSMIntegration**: `true`
        * **DeploySecurityHubIntegration**: `true`
      * Parameters related to the CloudTrail Integration:
        * **VisionOneAuthenticationToken**: Vision One Authentication Token. You can learn more about it [here](https://docs.trendmicro.com/en-us/enterprise/trend-vision-one-olh/administrative-setti/user-accounts/obtaining-api-keys-f_001.aspx)
        * **VisionOneRegion**: Vision One Region. ou can learn more about it [here](https://automation.trendmicro.com/xdr/Guides/Regional-Domains)
        * **ExistingOrganizationalCloudtrailBucketName**: Bucket name of an existing Organizational CloudTrail. You can learn more about it [here](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)
      * Parameters related to the SSM Integration:
        * **CronJob**: `cron(15 10 * * ? *)`
        * **AccountAdminStatus**: `SELF`
      * Parameters related to the SecurityHub Integration:
        * **EnableSecurityHub**: `false`, unless you don't have Security Hub enabled. `true` would enable Security Hub in the Audit Account

3. Choose both the **Capabilities** and select **Submit** to launch the stack.

    [] I acknowledge that AWS CloudFormation might create IAM resources with custom names.

    [] I acknowledge that AWS CloudFormation might require the following capability: CAPABILITY_AUTO_EXPAND

Wait for the CloudFormation status to change to `CREATE_COMPLETE` state.

## Launch using Customizations for Control Tower (CfCT)

{{% notice warning %}}
Deploying using Customizations for Control Tower (CfCT) is not yet supported for this ABI Module.
{{% /notice %}}

[Customizations for AWS Control Tower](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/) combines AWS Control Tower and other highly-available, trusted AWS services to help customers more quickly set up a secure, multi-account AWS environment using AWS best practices. You can easily add customizations to your AWS Control Tower landing zone using an AWS CloudFormation template and service control policies (SCPs). You can deploy the custom template and policies to individual accounts and organizational units (OUs) within your organization. It also integrates with AWS Control Tower lifecycle events to ensure that resource deployments stay in sync with your landing zone. For example, when a new account is created using the AWS Control Tower account factory, Customizations for AWS Control Tower ensures that all resources attached to the account's OUs will be automatically deployed.

The templates provided as part of the ABI packages are deployable using Customizations for Control Tower. Please check below for additional details.

### Pre-requisites

1. The CfCT solution, do not have ability to launch resources on the Management account. Hence, you need to create the role with required permissions in the Management account.

### How it works

To deploy this integration page using CfCT solution, add the following blurb to the `manifest.yaml` file from your CfCT solution and update the account/ou names as needed.

```
resources:
  - name: sra-enable-partner1-solution
    resource_file: https://aws-abi-pilot.s3.us-east-1.amazonaws.com/cfn-abi-trend-cloudone/main/templates/main.template.yaml
    deploy_method: stack_set
    parameters:
      - parameter_key: pProductArn
        parameter_value: arn:aws:securityhub:us-east-1::product/cloud-custodian/cloud-custodian
      - parameter_key: pSRASourceS3BucketName
        parameter_value: aws-abi-pilot
      - parameter_key: pSRAStagingS3KeyPrefix
        parameter_value: cfn-abi-aws-reference-guide
      - parameter_key: CloudOneApiKey
        parameter_value: Your Cloud One API Key. You can learn more about it [here](https://cloudone.trendmicro.com/docs/identity-and-account-management/c1-api-key/)
      - parameter_key: OrganizationId
        parameter_value: Your AWS Organization Id. You can learn how to find yours following [this](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_details.html) AWS documentation.
      - parameter_key: DeployCloudTrailIntegration
        parameter_value: true
      - parameter_key: DeploySSMIntegration
        parameter_value: true
      - parameter_key: DeploySecurityHubIntegration
        parameter_value: true
      - parameter_key: VisionOneAuthenticationToken
        parameter_value: Vision One Authentication Token. You can learn more about it [here](https://docs.trendmicro.com/en-us/enterprise/trend-vision-one-olh/administrative-setti/user-accounts/obtaining-api-keys-f_001.aspx)
      - parameter_key: VisionOneRegion
        parameter_value: Vision One Region. ou can learn more about it [here](https://automation.trendmicro.com/xdr/Guides/Regional-Domains)
      - parameter_key: ExistingOrganizationalCloudtrailBucketName
        parameter_value: Bucket name of an existing Organizational CloudTrail. You can learn more about it [here](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html)
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

**Next:** Choose [Postdeployment Options](/post-deployment-steps/index.html) to get started.
