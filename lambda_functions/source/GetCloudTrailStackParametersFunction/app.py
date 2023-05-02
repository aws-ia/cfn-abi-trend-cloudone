"""Custom Resource to get the CloudTrail Stack Parameters from Trend Cloud One.

Version: 1.0

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import json
import os
import re
import uuid
from urllib.parse import unquote
import urllib3
import cfnresponse
import boto3

def lambda_handler(event, context):
    status = cfnresponse.SUCCESS
    response_data = {}
    physicalResourceId = None
    try:
        
        if event["RequestType"] == "Create" or event["RequestType"] == "Update":
            cloudOneRegion = os.environ['CloudOneRegion']
            sm = boto3.client('secretsmanager')
            cloudOneApiKey = sm.get_secret_value(SecretId=os.environ['CloudOneApiKeySecret'])['SecretString']
            awsAccountId = os.environ['AwsAccountId']
            awsRegion = os.environ['AwsRegion']

            url = 'https://cloudtrail.'+cloudOneRegion+'.cloudone.trendmicro.com/api/stacks'

            payload = json.dumps({
                'providerAccountID': awsAccountId,
                'awsRegion': awsRegion
            })
            headers = {
                'api-version': 'v1',
                'Authorization': 'ApiKey '+cloudOneApiKey+'',
                'Content-Type': 'application/json'
            }

            http = urllib3.PoolManager()
            encoded_payload = payload.encode("utf-8")
            print(url)
            response = http.request("POST", url=url, headers=headers, body=encoded_payload)
            print(response)
            response_json_data = json.loads(response.data.decode("utf-8"))
            print(response_json_data)
            encodedDeploymentUrl = response_json_data["deploymentURL"]
            print(encodedDeploymentUrl)
            templateUrl = re.search(r"templateUrl=([^&]+)", encodedDeploymentUrl).group(1)
            s3BucketKey = re.search(r"param_S3BucketKey=([^&]+)", encodedDeploymentUrl).group(1)
            s3BucketName = re.search(r"param_S3BucketName=([^&]+)", encodedDeploymentUrl).group(1)
            serviceToken = re.search(r"param_ServiceToken=([^&]+)", encodedDeploymentUrl).group(1)
            serviceUrl = re.search(r"param_ServiceURL=([^&]+)", encodedDeploymentUrl).group(1)
            apiVersion = re.search(r"param_APIVersion=([^\n]+)", encodedDeploymentUrl).group(1)

            physicalResourceId = str(uuid.uuid4())
            response_data = {
                "TemplateUrl": templateUrl,
                "S3BucketKey": s3BucketKey,
                "S3BucketName": s3BucketName,
                "ServiceToken": serviceToken,
                "ServiceUrl": unquote(serviceUrl),
                "ApiVersion": apiVersion
            }

        else: # if event["RequestType"] == "Delete":
            physicalResourceId = event["PhysicalResourceId"]

    except Exception as exception:
        print(exception)
        status = cfnresponse.FAILED

    cfnresponse.send(event, context, status, response_data, physicalResourceId)