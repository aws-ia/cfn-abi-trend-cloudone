"""Custom Resource to get the Organizational Trail's Bucket Name.

Version: 1.0

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
import boto3
import cfnresponse

def lambda_handler(event, context):
    status = cfnresponse.SUCCESS
    response_data = {}
    physical_resource_id = None
    try:
        
        if event["RequestType"] == "Create" or event["RequestType"] == "Update":
        
            # List all CloudTrail trails and find the one that has IsOrganizationTrail set to True
            cloud_trail_client = boto3.client('cloudtrail')
            cloud_trail_trails = cloud_trail_client.describe_trails()
            cloud_trail_trails = cloud_trail_trails["trailList"]
            trail_name = ""
            trail_bucket_name = ""
            for trail in cloud_trail_trails:
                if trail["IsOrganizationTrail"] is True:
                    trail_name = trail["Name"]
                    trail_bucket_name = trail["S3BucketName"]
                    break
            
            if not (trail_name or trail_bucket_name):
                raise Exception("There is no organizational CloudTrail")
            
            physical_resource_id = trail_name
            response_data = {
                "TrailName": trail_name,
                "BucketName": trail_bucket_name,
            }
            print(response_data)
            
        else: # if event["RequestType"] == "Delete":
            physical_resource_id = event["PhysicalResourceId"]

    except Exception as exception:
        print(exception)
        status = cfnresponse.FAILED
    
    cfnresponse.send(event, context, status, response_data, physical_resource_id)
