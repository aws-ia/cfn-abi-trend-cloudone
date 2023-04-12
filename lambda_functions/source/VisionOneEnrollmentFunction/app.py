"""Custom Resource to enroll a Trend Cloud One account to a Trend Vision One account.

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
        cloudOneRegion = os.environ['CloudOneRegion']
        cloudOneApiKey = os.environ['CloudOneApiKey']
        visionOneServiceToken = os.environ['VisionOneServiceToken']

        headers = {
        'api-version': 'v1',
        'Authorization': 'ApiKey '+cloudOneApiKey+'',
        'Content-Type': 'application/json'
        }

        http = urllib3.PoolManager()
        
        if event["RequestType"] == "Create" or event["RequestType"] == "Update":
        

            url = 'https://visionone-connect.'+cloudOneRegion+'.cloudone.trendmicro.com/api/connectors'

            payload = json.dumps({
                'enrollmentToken': visionOneServiceToken
            })
            
            encoded_payload = payload.encode("utf-8")
            print(url)
            response = http.request("POST", url=url, headers=headers, body=encoded_payload)
            print(response)
            response_json_data = json.loads(response.data.decode("utf-8"))
            print(response_json_data)
            physicalResourceId = response_json_data["registration"]["status"] 
            response_data = {"ID": response_json_data["registration"]["status"]}

        else: # if event["RequestType"] == "Delete":
            physicalResourceId = event["PhysicalResourceId"]

    except Exception as exception:
        print(exception)
        status = cfnresponse.FAILED
    
    cfnresponse.send(event, context, status, response_data, physicalResourceId)