"""Custom Resource to get a Trend Cloud One Workload Security account's External Id.

Version: 1.0

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import json
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
            cloudOneApiKey = sm.get_secret_value(SecretId=event['ResourceProperties']['CloudOneApiKeySecret'])['SecretString']
            cloudOneRegion = event['ResourceProperties']['CloudOneRegion']

            url = 'https://workload.'+cloudOneRegion+'.cloudone.trendmicro.com/api/awsconnectorsettings'

            headers = {
                'api-version': 'v1',
                'Authorization': 'ApiKey '+cloudOneApiKey+'',
                'Content-Type': 'application/json'
            }

            http = urllib3.PoolManager()
            print (url)
            response = http.request("GET", url=url, headers=headers)
            response_json_data = json.loads(response.data.decode("utf-8"))
            print(response_json_data["externalId"])
            physicalResourceId = response_json_data["externalId"] 
            response_data = {"ExternalID": response_json_data["externalId"]}

        else: # if event["RequestType"] == "Delete":
            physicalResourceId = event["PhysicalResourceId"]

    except Exception as exception:
        print(exception)
        status = cfnresponse.FAILED
    
    cfnresponse.send(event, context, status, response_data, physicalResourceId)