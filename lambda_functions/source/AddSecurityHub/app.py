import boto3
import os
import urllib3
import json
import time

# Cloud One API Key
cloud_one_api_key = os.environ['CloudOneApiKey']
cloud_one_region = os.environ['CloudOneRegion']
enable_security_hub = os.environ['EnableSecurityHub']



# Initialize the AWS SDK
client = boto3.client('securityhub')

# Get the AWS account ID and region
aws_account_id = boto3.client('sts').get_caller_identity().get('Account')
aws_region = boto3.session.Session().region_name

# ARN used to get the list of activated products
get_tm_arn = "arn:aws:securityhub:"+aws_region+":"+aws_account_id+":product-subscription/trend-micro/cloud-one"

# ARN used to add the product to the list of activated products
add_tm_arn = "arn:aws:securityhub:"+aws_region+"::product/trend-micro/cloud-one"

# Check if Security Hub is enabled in the account, in case not enable it
try:
  response = client.describe_hub()
  if response['HubArn'] is not None:
    print("Security Hub is enabled")
except Exception as e:
    if enable_security_hub == "true":
        print("Security Hub is not enabled, enabling now")
        enable_security_hub = client.enable_security_hub(EnableDefaultStandards=False)
        if enable_security_hub['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("Security Hub is now enabled")
    else:
        print("Security Hub is not enabled, please enable it to continue")

# Wait 2 seconds to make sure the product is enabled
time.sleep(2)

# Get the list of activated products
list_activated_product = client.list_enabled_products_for_import().get('ProductSubscriptions')

# Check if the product is already in the list of activated products, if not add it
if get_tm_arn in list_activated_product:
    print(f"The arn {get_tm_arn} exists in the list, no action is required.")
else:
    print(f"The arn {get_tm_arn} does not exist in the list, adding it now.")
    add_tm_product = client.enable_import_findings_for_product(ProductArn=add_tm_arn)
    print(f"Success")

# Add Security Hub integration to Cloud One
http = urllib3.PoolManager()

# Headers for the GET and POST requests
get_header = {
        'api-version': 'v1',
        'Authorization': 'ApiKey '+cloud_one_api_key+''
    }
post_header = {
        'api-version': 'v1',
        'Authorization': 'ApiKey '+cloud_one_api_key+'',
        'Content-Type': 'application/json'
    }

# URL for the GET and POST requests
url = "https://integrations."+cloud_one_region+".cloudone.trendmicro.com/api/integrations"

# Get the list of integrations
get_sechub_integration = http.request('GET', url, headers=get_header)
get_sechub_integration = json.loads(get_sechub_integration.data.decode('utf-8'))
get_sechub_integration = get_sechub_integration["integrations"]

# Payload to add the Security Hub integration
payload = {
"name": f"Security Hub Integration - {aws_account_id}",
"description": f"This is an integration to send events from container security to security hub for the AWS Account Id {aws_account_id}",
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
for item in get_sechub_integration:
    if item['configuration']['awsAccountId'] == aws_account_id:
        print(f"There is already an integration for the AWS Account ID {aws_account_id}")
        break
else:
    print(f"No match found for ID {aws_account_id}, adding integration now.")
    add_sechub_integration = http.request('POST', url, headers=post_header, body=json.dumps(payload))
    add_sechub_integration = json.loads(add_sechub_integration.data.decode('utf-8'))
    integration_id = add_sechub_integration["id"]
    print(f"Success, the integration Id is: {integration_id}")


