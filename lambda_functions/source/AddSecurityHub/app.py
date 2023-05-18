"""Custom Resource to enable Trend Cloud One in Security Hub.
Version: 1.0

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import json
import os
import urllib3
import cfnresponse
import boto3

# Initialize the SecurityHub SDK
security_hub_client = boto3.client('securityhub')

# Get the AWS account ID and region
aws_account_id = boto3.client('sts').get_caller_identity().get('Account')
aws_region = boto3.session.Session().region_name

# ARN used to get the list of activated products
get_tm_arn = "arn:aws:securityhub:"+aws_region+":"+aws_account_id+":product-subscription/trend-micro/cloud-one"

# ARN used to add the product to the list of activated products
add_tm_arn = os.environ['CloudOneProductArn']

cloud_one_region = os.environ['CloudOneRegion']
sm = boto3.client('secretsmanager')
cloudOneApiKey = sm.get_secret_value(SecretId=os.environ['CloudOneApiKeySecret'])['SecretString']

headers = {
    'api-version': 'v1',
    'Authorization': 'ApiKey '+cloudOneApiKey+'',
    'Content-Type': 'application/json'
}

http = urllib3.PoolManager()

url = "https://integrations."+cloud_one_region+".cloudone.trendmicro.com/api/integrations"

def is_security_hub_enabled():
    '''
    Return True if Security Hub is enabled in the account, False otherwise.
    '''
    try:
        response = security_hub_client.list_enabled_products_for_import()
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
    except Exception as exception:
        print(exception)
        return False

def list_enabled_products_for_import():
    '''
    Return the list of products enabled for import.
    '''
    enabled_list = []
    paginator = security_hub_client.get_paginator('list_enabled_products_for_import')
    for page in paginator.paginate():
        enabled_list += page['ProductSubscriptions']
    return enabled_list

def initialize_integration():
    '''
    Initialize the integration between Trend Cloud One and Security Hub.
    '''

    if is_security_hub_enabled():
        # Get the list of activated products
        list_activated_product = list_enabled_products_for_import()

        # Check if the product is already in the list of activated products, if not add it

        if get_tm_arn in list_activated_product:
            print(f"The arn {get_tm_arn} exists in the list, no action is required.")
        else:
            try:
                print(f"The arn {get_tm_arn} does not exist in the list, adding it now.")
                security_hub_client.enable_import_findings_for_product(ProductArn=add_tm_arn)
            except Exception as exception:
                raise exception
            
        # Get the list of integrations
        get_sechub_integration = http.request('GET', url, headers=headers)
        get_sechub_integration = json.loads(get_sechub_integration.data.decode('utf-8'))
        get_sechub_integration = get_sechub_integration["integrations"]

        # Payload to add the Security Hub integration
        payload = {
            "name": f"Security Hub Integration - {aws_account_id}",
            "description": f"This is an integration to send events from Trend Cloud One to Security Hub for the AWS Account Id {aws_account_id}",
            "type": "SECURITY_HUB",
            "configuration": {
                "awsRegion": f"{aws_region}",
                "awsAccountId": f"{aws_account_id}"
            },
            "filters": {
                "serviceIds": [],
                "severityIds": []
            }
        }

        # Check if there is already an integration for the AWS Account ID, in case not add it
        integration_id = None
        for item in get_sechub_integration:
            if item['configuration']['awsAccountId'] == aws_account_id:
                print(f"There is already an integration for the AWS Account ID {aws_account_id}")
                break
        else:
            print(f"No match found for ID {aws_account_id}, adding integration now.")
            add_sechub_integration = http.request('POST', url, headers=headers, body=json.dumps(payload))
            add_sechub_integration = json.loads(add_sechub_integration.data.decode('utf-8'))
            integration_id = add_sechub_integration["id"]
    else:
        print("Security Hub is not enabled in this account, no action is required.")

    print(f"The integration Id is: {integration_id}")
    return integration_id

def remove_integration(integration_id):
    '''
    Remove the integration between Trend Cloud One and Security Hub.
    '''

    if is_security_hub_enabled():
        try:

            # Deactivate the product
            security_hub_client.disable_import_findings_for_product(ProductSubscriptionArn=get_tm_arn)
            
            # Delete integration on Cloud One
            delete_sechub_integration = http.request('DELETE', f"{url}/{integration_id}", headers=headers)
            delete_sechub_integration = json.loads(delete_sechub_integration.data.decode('utf-8'))
            print(delete_sechub_integration)
        except Exception as exception:
            print(exception)
            raise exception
    else:
        print("Security Hub is not enabled in this account, no action is required.")

def lambda_handler(event, context):
    status = cfnresponse.SUCCESS
    response_data = {}
    physicalResourceId = None
    try:
        
        if event["RequestType"] == "Create":
            integration_id = initialize_integration()
            physicalResourceId = integration_id 
            response_data = {"ID": integration_id}
            
        elif event["RequestType"] == "Update":
            integration_id = event["PhysicalResourceId"]
            remove_integration(integration_id)
            integration_id = initialize_integration()
            physicalResourceId = integration_id
            response_data = {"ID": physicalResourceId}

        else: # if event["RequestType"] == "Delete":
            integration_id = event["PhysicalResourceId"]
            remove_integration(integration_id)
        
    except Exception as exception:
        print(exception)
        status = cfnresponse.FAILED
    
    cfnresponse.send(event, context, status, response_data, physicalResourceId)
