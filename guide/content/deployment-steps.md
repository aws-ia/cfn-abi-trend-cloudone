---
weight: 8
title: Deployment Steps
description: Step-by-step instructions for deploying the <project-name>.
---

<<<<<<< before updating
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
=======
## Launch the CloudFormation template in the management account


1. Download the Cloudformation template from the following location: https://<abi-template-location>
2. Launch CloudFormation template in your AWS Control Tower home region.
    * Stack name: `template-<partner-name>-enable-integrations`
    * List parameters with [default values and update below example as needed]
        * **EnableIntegrationsStackName**: `template-<partner-name>-enable-integrations`
        * **EnableIntegrationsStackRegion**: `us-east-1`
        * **EnableIntegrationsStackSetAdminRoleName**: `AWSCloudFormationStackSetAdministrationRole`
        * **EnableIntegrationsStackSetExecutionRoleName**: `AWSCloudFormationStackSetExecutionRole`
        * **EnableIntegrationsStackSetExecutionRoleArn**: `arn:aws:iam::<account-id>:role/AWSCloudFormationStackSetExecutionRole`
>>>>>>> after updating

3. Select both the **Capabilities** and choose **Submit** to launch the stack.

    [] I acknowledge that AWS CloudFormation might create IAM resources with custom names.

    [] I acknowledge that AWS CloudFormation might require the following capability: CAPABILITY_AUTO_EXPAND

Wait for the CloudFormation status to change to `CREATE_COMPLETE` state.

<<<<<<< before updating
## Launch using Customizations for Control Tower (CfCT)

{{% notice warning %}}
Deploying using Customizations for Control Tower (CfCT) is not yet supported for this ABI Module.
{{% /notice %}}
=======

## Launch using Customizations for Control Tower
>>>>>>> after updating

[Customizations for AWS Control Tower](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/) (CfCT) combines AWS Control Tower and other AWS services to help you set up an AWS environment. You can deploy the templates provided with the ABI solution using CfCT.

The templates provided as part of the ABI solution are deployable using Customizations for Control Tower. Please check below for additional details.

### Pre-requisites

1. The CfCT solution, do not have ability to launch resources on the Management account. Hence, you need to create the role with required permissions in the Management account.

### How it works

<<<<<<< before updating
To deploy this integration page using CfCT solution, add the following blurb to the `manifest.yaml` file from your CfCT solution and update the account/ou names as needed.
=======
To deploy the sample partner integration page using CfCT solution, add the following blurb to the `manifest.yaml` file from your CfCT solution and then update the account and organizational unit (OU) names as needed.
>>>>>>> after updating

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
## Partner specific steps [UPDATE AS NEEDED]
After the stack deployment is complete, verfiy following resources [....]:

  - <resource-1>
  - <resource-2>

Open <partner-console> and navigate to <section> and perform following steps:
   1. <step-1>
   2. <step-2>

<<<<<<< before updating
**Next:** Choose [Postdeployment Options](/post-deployment-steps/index.html) to get started.
=======

**Next:** Go to [Postdeployment steps](/post-deployment-steps/index.html) to verify the deployment.
>>>>>>> after updating
