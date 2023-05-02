"""Custom Resource to get the Trend Cloud One region and account id.

Version: 1.0

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import json
import os
import urllib3
import cfnresponse
import boto3

def lambda_handler(event, context):
    status = cfnresponse.SUCCESS
    response_data = {}
    physicalResourceId = None
    try:
        
        if event["RequestType"] == "Create" or event["RequestType"] == "Update":
            sm = boto3.client('secretsmanager')
            cloudOneApiKey = sm.get_secret_value(SecretId=os.environ['CloudOneApiKeySecret'])['SecretString']
            apiKeyId = cloudOneApiKey.split(':')[0]

            url = 'https://accounts.cloudone.trendmicro.com/api/apikeys/' + apiKeyId

            headers = {
                'api-version': 'v1',
                'Authorization': 'ApiKey '+cloudOneApiKey+'',
                'Content-Type': 'application/json'
            }

            http = urllib3.PoolManager()
            print(url)
            response = http.request("GET", url=url, headers=headers)
            print(response)
            response_json_data = json.loads(response.data.decode("utf-8"))
            print(response_json_data)
            urn = response_json_data["urn"]
            region = urn.split(":")[3]
            accountId = urn.split(":")[4]
            physicalResourceId = response_json_data["urn"] 
            response_data = {"AccountId": accountId, "Region": region}

        else: # if event["RequestType"] == "Delete":
            physicalResourceId = event["PhysicalResourceId"]

    except Exception as e:
        print(e)
        status = cfnresponse.FAILED
    
    cfnresponse.send(event, context, status, response_data, physicalResourceId)