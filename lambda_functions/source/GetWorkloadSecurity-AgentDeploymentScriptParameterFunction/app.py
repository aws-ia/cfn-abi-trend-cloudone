import urllib3
import json
import boto3
import os
http = urllib3.PoolManager()
import re
import cfnresponse

# set variables
url = os.environ['C1_API_ENDPOINT']
api_key = os.environ['C1_API_KEY']

# Create an AWS Organizations client
org_client = boto3.client('organizations')

# Retrieve the root ID of the organization
root_id = org_client.list_roots()['Roots'][0]['Id']

# Recursive function to retrieve all OU IDs in the organization
def get_all_ou_ids(parent_id):
    ou_ids = []
    paginator = org_client.get_paginator('list_organizational_units_for_parent')
    response_iterator = paginator.paginate(
        ParentId=parent_id,
        PaginationConfig={
            'PageSize': 20
        }
    )
    for page in response_iterator:
        for ou in page['OrganizationalUnits']:
            ou_ids.append(ou['Id'])
            ou_ids += get_all_ou_ids(ou['Id'])
    return ou_ids

# Call the function to retrieve all OU IDs in the organization
all_ou_ids = get_all_ou_ids(root_id)

def lambda_handler(event, context):
    print(event)
    status = cfnresponse.SUCCESS
    response_data = {}
    physicalResourceId = None
    try:
        if event["RequestType"] == "Create" or event["RequestType"] == "Update":
            
            # get secret
            client = boto3.client('secretsmanager')
            secrets = client.get_secret_value(SecretId=api_key)
            secrets_manager = json.loads(secrets["SecretString"])
            cloud_one_api_key = secrets_manager["c1apikey"]
            
            # Base Deployment Script generation to get params.
            payload = json.dumps({
            "platform": "linux",
            "validateCertificateRequired": True,
            "validateDigitalSignatureRequired": True,
            "activationRequired": True,
            "policyID": 0,
            "relayGroupID": 0,
            "computerGroupID": 0
            })
            # set request headers to send to ws api
            headers = {
            'Authorization': "ApiKey "+ cloud_one_api_key,
            'api-version': 'v1',
            'Content-Type': 'application/json'
            }

            response = http.request("POST", url, headers=headers, body=payload)
            response_str = response.data.decode('utf-8') # convert response to string
            #Filter response values for ACTIVATIONURL, MANAGERURL, TenantID, and Token using regular expressions
            activation_url = re.search(r"ACTIVATIONURL='(.+?)'", response_str).group(1)
            manager_url = re.search(r"MANAGERURL='(.+?)'", response_str).group(1)
            tenant_id = re.search(r'tenantID:(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})', response_str).group(1)
            token = re.search(r'token:([\w-]+)', response_str).group(1)
            ou_ids_str = ', '.join(all_ou_ids)
            ou_ids_str = ou_ids_str.replace('[','').replace(']','').replace("'","")
            
            response_data = {"ActivationURL": activation_url, "ManagerURL": manager_url, "TenantID": tenant_id,"Token": token, "OrganizationalUnits": str(ou_ids_str)}
            
        else: # if event["RequestType"] == "Delete":
            physicalResourceId = event["PhysicalResourceId"]
    
    except Exception as e:
        print(e)
        status = cfnresponse.FAILED

    cfnresponse.send(event, context, status, response_data, physicalResourceId)