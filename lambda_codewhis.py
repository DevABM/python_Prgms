# create a lambda function to create S3 bucket with the name my-4th-bucket-whisper and return response


import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket='my-4th-bucket-whisper4')
    
    #upload a file text.txt to s3 bucket my-4th-bucket-whisper
    s3.upload_file('text.txt', 'my-4th-bucket-whisper4', 'text1.txt')
    
    #upload an object to s3 bucket my-4th-bucket-whisper
    s3.put_object(Bucket='my-4th-bucket-whisper4', Key='text2.txt', Body="This is an experiment")
    
    # update the lambda function addObjects to enable versioning for the bucket my-4th-bucket-whisper4
    s3.put_bucket_versioning(Bucket='my-4th-bucket-whisper4', VersioningConfiguration={'Status': 'Enabled'})
    
    
    return response