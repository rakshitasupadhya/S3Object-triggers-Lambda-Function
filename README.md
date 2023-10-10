# S3Object-triggers-Lambda-Function
This is a demonstartion on how S3 Object triggers lambda function and displays the contents on CloudWatch

# Requirement
This sample project depends on boto3, the AWS SDK for Python, and requires Python 2.6.5+, 2.7, 3.3, 3.4, or 3.5. You can install boto3 using pip:

pip install boto3

# Project Execution
1. Create S3 Bucket
2. Create Lambda function and add Role - S3ReadOnlyAccess policy to it
3. Add trigger event in S3 under Permission tab
4. Trigger must be updated automatically in Lambda
5. Upload Transaction file in S3 and check the CloudWatch for results
