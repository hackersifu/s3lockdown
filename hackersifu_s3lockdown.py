import boto3
import json
import sys

#The default lambda_handler name is used here for simplicity, but can be modified.
def lambda_handler(event, context):
    # The following code is designed to be invoked through a CloudWatch rule.
    # The varible s3 is used in the to call the s3.buckets.all function, and the client is used within the client.put_public_access_block function.
    s3 = boto3.resource('s3')
    client = boto3.client('s3')
    # You can use the print function to look at the output of which buckets will be closed. This can be used within Lambda for testing the script. This can be removed to limit the amount of calls to each bucket.
    for bucket in s3.buckets.all():
      print(bucket.name)
    # This is the part of the code that will complete the closure of the buckets from public access.
    for bucket in s3.buckets.all():
      response = client.put_public_access_block(
          Bucket=bucket.name,
          PublicAccessBlockConfiguration={
              'BlockPublicAcls': True,
              'IgnorePublicAcls': True,
              'BlockPublicPolicy': True,
              'RestrictPublicBuckets': True
    }
)
    # Response code to show that the code works during testing.
    return {
        'statusCode': 200,
        'body': json.dumps('Your buckets are secure from the hacks!')
    
    }
    sys.exit()