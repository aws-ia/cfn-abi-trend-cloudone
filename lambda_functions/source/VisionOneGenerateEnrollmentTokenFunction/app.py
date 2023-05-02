"""Custom Resource to generate and delete a Trend Vision One Enrollment Token.

Version: 1.0

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import json
import os
import urllib3
import cfnresponse
import boto3

def define_endpoint(region):
    if region == "Australia":
        return "https://api.au.xdr.trendmicro.com"
    elif region == "European Union":
        return "https://api.eu.xdr.trendmicro.com"
    elif region == "India":
        return "https://api.in.xdr.trendmicro.com"
    elif region == "Japan":
        return "https://api.xdr.trendmicro.co.jp"
    elif region == "Singapore":
        return "https://api.sg.xdr.trendmicro.com"
    elif region == "United States":
        return "https://api.xdr.trendmicro.com"
    raise Exception("Invalid region")

def lambda_handler(event, context):
    status = cfnresponse.SUCCESS
    response_data = {}
    physicalResourceId = None
    try:
        sm = boto3.client('secretsmanager')
        visionOneAuthenticationToken = sm.get_secret_value(SecretId=os.environ['VisionOneAuthenticationTokenSecret'])['SecretString']
        visionOneRegion = os.environ['VisionOneRegion']

        headers = {
            'Authorization': 'Bearer ' + visionOneAuthenticationToken,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        http = urllib3.PoolManager()
        url = define_endpoint(visionOneRegion)   
        
        if event["RequestType"] == "Create" or event["RequestType"] == "Update":
            
            payload = json.dumps({
            'productId': 'scc'
            })
            url = url + "/v1.0/preview/uic/instances/enrollment"
            encoded_payload = payload.encode("utf-8")
            print(url)
            response = http.request("POST", url=url, headers=headers, body=encoded_payload)
            print(response)
            response_json_data = json.loads(response.data.decode("utf-8"))
            print(response_json_data)
            physicalResourceId = str(response_json_data["connectorId"])
            response_data = {
            "token": response_json_data["token"],
            "connectorId": response_json_data["connectorId"],
            "tokenExpireTime": response_json_data["tokenExpireTime"]
            }

        else: # if event["RequestType"] == "Delete":
            physicalResourceId = event["PhysicalResourceId"]
            connectorId = physicalResourceId
            url = url + "/v2.0/xdr/portal/connectors/onpremise/" + connectorId
            response = http.request("DELETE", url=url, headers=headers)
            print(response)
            response_json_data = json.loads(response.data.decode("utf-8"))
            print(response_json_data)

    except Exception as e:
        print(e)
        status = cfnresponse.FAILED
    
    cfnresponse.send(event, context, status, response_data, physicalResourceId)