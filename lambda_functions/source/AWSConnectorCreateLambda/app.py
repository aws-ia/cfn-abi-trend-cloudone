"""Custom Resource to add an AWS Account to Trend Cloud One Workload Security.

Version: 1.0

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import json
import urllib3
import cfnresponse
import os
import boto3

def lambda_handler(event, context):
    
    status = cfnresponse.SUCCESS
    response_data = {}
    physicalResourceId = None

    accountId = os.environ['awsaccountid']
    crossAccountRoleArn = os.environ['crossaccountrolearn']
    sm = boto3.client('secretsmanager')
    cloudOneApiKey = sm.get_secret_value(SecretId=event['ResourceProperties']['CloudOneApiKeySecret'])['SecretString']
    cloudOneRegion = event['ResourceProperties']['CloudOneRegion']

    headers = {
        'api-version': 'v1',
        'Authorization': 'ApiKey '+cloudOneApiKey+'',
        'Content-Type': 'application/json'
    }

    http = urllib3.PoolManager()

    try:
        if event["RequestType"] == "Create" or event["RequestType"] == "Update":
            
            url = 'https://workload.'+cloudOneRegion+'.cloudone.trendmicro.com/api/awsconnectors'

            payload = json.dumps({
            "displayName": accountId,
            "accountId": accountId,
            "crossAccountRoleArn": crossAccountRoleArn                                                                                        
            })

            encoded_payload = payload.encode("utf-8")
            response = http.request("POST", url=url, headers=headers, body=encoded_payload)

            response_json_data = json.loads(response.data.decode("utf-8"))
            print(response_json_data)
            physicalResourceId = str(response_json_data["ID"]) 
            response_data = {"ID": str(response_json_data["ID"])}

        else: # if event["RequestType"] == "Delete":
            ID = event["PhysicalResourceId"]

            url = 'https://workload.'+cloudOneRegion+'.cloudone.trendmicro.com/api/awsconnectors/'+ID
            response = http.request("DELETE", url=url, headers=headers)
            print(response.data.decode("utf-8"))

    except Exception as exception:
        print(exception)
        status = cfnresponse.FAILED
    
    cfnresponse.send(event, context, status, response_data, physicalResourceId)