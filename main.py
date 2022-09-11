import requests
import boto3
import os

bucket_name = os.environ.get('BUCKET_NAME')
content = requests.get('https://data.gharchive.org/2015-01-01-15.json.gz').content
s3_client = boto3.client('s3')
s3_client.put_object(
    Body=content,
    Bucket=bucket_name,
    Key='lambdademo/2015-01-01-15.json.gz'
)
