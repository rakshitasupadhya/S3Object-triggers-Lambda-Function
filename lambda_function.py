import json
import boto3
import urllib.parse
 
print("loading function")
 
s3=boto3.client('s3')
 
def lambda_handler(event, context):
    
    print(f"event: {event}")
    
    bucket= event['Records'][0]['s3']['bucket']['name'] 
    
    
    key= urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
   
    response=s3.get_object(Bucket=bucket, Key=key)
    
    content=response['Body']
    jsonObject=json.loads(content.read())
    Transaction=jsonObject['Transaction']
    
    for record in Transaction:
        print("TransactionType: "+record['transtype'])
        print("Transaction AMount: "+ str(record['amount']))
        print("-------")
