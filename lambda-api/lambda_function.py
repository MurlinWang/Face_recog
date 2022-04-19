import json
import boto3
import base64

def lambda_handler(event, context):
    # Set S3 Bucket Parameters
    s3BucketName = "<demo-files-bucket-name>" # TODO
    
    # POST method
    if event:
       print('This is a POST request')
       
       fileName = event['fileName']
       print(fileName)
       
       client = boto3.client('s3')
       response = client.get_object(Bucket=s3BucketName, Key=fileName)
       
       bytesData = response['Body'].read()
       data = base64.b64encode(bytesData).decode("utf8")
       print(data) # bytes data check
       
       return {
           'statusCode': 200,
           'body': json.dumps({"bytesData": data, "fileType": response['ContentType']})
       }
    
    # GET method
    else:
        print('This is a GET request')
        fileList = []
        
        # Go thru S3 bucket
        client = boto3.client('s3')
        response = client.list_objects_v2(Bucket=s3BucketName)
        
        for object in response['Contents']:
            fileList.append(object['Key'])
        
        print(fileList) # file list check
        
        return {
            'statusCode': 200,
            'body': json.dumps({"s3Files": fileList})
        }
        
