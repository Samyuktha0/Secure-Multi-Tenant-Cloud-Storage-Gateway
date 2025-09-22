import boto3

s3 = boto3.client('s3')

def upload_file(filename, data):
    s3.put_object(Bucket='secure-bucket', Key=filename, Body=data)

def download_file(filename):
    obj = s3.get_object(Bucket='secure-bucket', Key=filename)
    return obj['Body'].read()
