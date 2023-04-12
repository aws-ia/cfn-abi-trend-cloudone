"""Custom Resource to add an AWS Account to Trend Cloud One.

Version: 1.0

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import json
import os
import urllib3
import cfnresponse

def lambda_handler(event, context):
    status = cfnresponse.SUCCESS
    response_data = {}
    physicalResourceId = None
    try:

        cloudOneRoleArn = os.environ['CloudOneRoleArn']
        cloudOneRegion = os.environ['CloudOneRegion']
        cloudOneApiKey = os.environ['CloudOneApiKey']

        headers = {
            'api-version': 'v1',
            'Authorization': 'ApiKey '+cloudOneApiKey+'',
            'Content-Type': 'application/json'
        }

        http = urllib3.PoolManager()
        
        
        if event["RequestType"] == "Create" or event["RequestType"] == "Update":
        
            url = 'https://cloudaccounts.'+cloudOneRegion+'.cloudone.trendmicro.com/api/cloudaccounts/aws'

            payload = json.dumps({
                'roleARN': cloudOneRoleArn
            })
            encoded_payload = payload.encode("utf-8")
            print(url)
            response = http.request("POST", url=url, headers=headers, body=encoded_payload)
            print(response)
            response_json_data = json.loads(response.data.decode("utf-8"))
            print(response_json_data)
            physicalResourceId = response_json_data["id"] 
            response_data = {"ID": response_json_data["id"]}

        else: # if event["RequestType"] == "Delete":
            id = event["PhysicalResourceId"]

            url = 'https://cloudaccounts.'+cloudOneRegion+'.cloudone.trendmicro.com/api/cloudaccounts/aws/' + id

            print(url)
            response = http.request("DELETE", url=url, headers=headers)
            print(response)
        
    except Exception as exception:
        print(exception)
        status = cfnresponse.FAILED
    
    cfnresponse.send(event, context, status, response_data, physicalResourceId)