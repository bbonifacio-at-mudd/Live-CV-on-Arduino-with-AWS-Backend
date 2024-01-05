import json
import base64
import json
import boto3
from botocore.exceptions import ClientError
import base64
from datetime import datetime

import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    http_method = event['requestContext']['http']['method']
    
    if http_method == "POST":
        #Intending to post data. Extract data and key
        try:
            #Set variables
            bucket = "saltinedatabase"
            
            #extract data
            body = event['body']
            body_decoded = base64.b64decode(body)
            body_string = body_decoded.decode('utf-8')  # Convert bytes to string
            body_dict = json.loads(body_string)  # Parse JSON string to a dictionary
            
            image_data = body_dict['image_data']
            metadata = body_dict['metadata']
            key = metadata['name']
            
            #See if the key is in the S3. If it is, raise
            try:
                print("trying")
                response = s3.head_object(Bucket=bucket, Key=key)
                return {
                'statusCode': 500,
                'body': json.dumps(f"This image already exists in the database: {key}")
                }
            except:
                #Image is not in the database: write
                response = s3_client.put_object(
                Body = image_data, 
                Bucket = bucket,
                Key = key,
                )
                return {
                    'statusCode': 200, 
                    'body': json.dumps(f'Image Posted Successfully: {key}')
                }
        except:
                return {
                'statusCode': 500,
                'body': json.dumps('Failed in Lambda Post')
                }
            
    
 


   
    
    # TODO implement
    print("event", event)

    #http_method = event['httpMethod']
    #print("http_method", http_method)
    
    body = event['body']
    print("body", body)
    
    body_decoded = base64.b64decode(body)
    body_string = body_decoded.decode('utf-8')  # Convert bytes to string
    body_dict = json.loads(body_string)  # Parse JSON string to a dictionary

    print("body_dict", body_dict)
    
    
    image_data = body_dict['image_data']
    metadata = body_dict['metadata']
    key = metadata['name']
    
    
    
    
    #body = json.loads(event['body'])
    #print("This is the body", body)
    #image_data = body['image_data']  # base64 encoded string
    more_binary_data = b'Here we have some more data'
    ms = image_data#more_binary_data#base64.b64decode(more_binary_data)
    response = s3_client.put_object(
        Body = ms, 
        Bucket = 'saltinedatabase',
        Key = key,
        )
    print(response)
    
    return {
        'statusCode': 200, 
        'body': json.dumps('Image Uploaded Successfully')
    }
























import json
import boto3
from botocore.exceptions import ClientError
import base64
from datetime import datetime

# Initialize Boto3 clients for S3 and RDS
s3_client = boto3.client('s3')
rds_client = boto3.client('rds')

def lambda_handler(event, context):
    
    http_method = event['httpMethod']
    
    if http_method == 'POST':
        try:
            
            # Parse the stringified 'body' into a JSON object
            body = json.loads(event['body'])
            image_data = body['image_data']  # base64 encoded string
            metadata = body['metadata']

            # Decode the base64 string to bytes
            image_bytes = base64.b64decode(image_data)
            more_binary_data = b'Here we have some more data'
            key_name = f"test-image-{datetime.utcnow().isoformat()}.png"

            # Upload the image to S3
            #s3_client.put_object(Body = more_binary_data, Bucket='saltinedatabase', Key=key_name)
            #client.put_object(Body=more_binary_data, Bucket='my_bucket_name', Key='my/key/including/anotherfilename.txt')
            
            # Boto 2.x
            from boto.s3.key import Key
            key = Key('hello.txt')
            key.set_contents_from_file('/tmp/hello.txt')
            
            # Boto 3
            s3.Object('mybucket', 'hello.txt').put(Body=open('/tmp/hello.txt', 'rb'))
            
            
        except:
            return {
                'statusCode': 200, 
                'body': json.dumps("Post Failed in DataLambda")
                }
                    
    
    
    return {
            'statusCode': 200,
            'body': json.dumps("End of DataLambda")
            }




import json
import boto3
from botocore.exceptions import ClientError
import base64
from datetime import datetime

# Initialize Boto3 clients for S3 and RDS
s3_client = boto3.client('s3')
rds_client = boto3.client('rds')

def lambda_handler(event, context):
    
    http_method = event['httpMethod']
    
    if http_method == 'POST':
        try:
            
            # Parse the stringified 'body' into a JSON object
            body = json.loads(event['body'])
            image_data = body['image_data']  # base64 encoded string
            metadata = body['metadata']

            # Decode the base64 string to bytes
            #image_bytes = base64.b64decode(image_data)
            #more_binary_data = b'Here we have some more data'
            #key_name = f"test-image-{datetime.utcnow().isoformat()}.png"

            # Upload the image to S3
            #s3_client.put_object(Body = more_binary_data, Bucket='saltinedatabase', Key=key_name)
            #client.put_object(Body=more_binary_data, Bucket='my_bucket_name', Key='my/key/including/anotherfilename.txt')
            
            # Boto 2.x
            from boto.s3.key import Key
            key = Key('hello.txt')
            key.set_contents_from_file('/tmp/hello.txt')
            
            # Boto 3
            s3.Object('saltinedatabase', 'hello.txt').put(Body=open('/tmp/hello.txt', 'rb'))
            
            
        except:
            s3.Object('saltinedatabase', 'hello.txt').put(Body=open('/tmp/hello.txt', 'rb'))
            return {
                'statusCode': 200, 
                'body': json.dumps("Post Failed in DataLambda")
                }
                    
    
    
    return {
            'statusCode': 200,
            'body': json.dumps("End of DataLambda")
            }





import json
import json
import boto3
from botocore.exceptions import ClientError
import base64
from datetime import datetime

client-boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    #Get the data
    body = json.loads(event['body'])
    image_data = body['image_data']  # base64 encoded string
    metadata = body['metadata']
    
    # Decode the base64 string to bytes
    image_bytes = base64.b64decode(image_data)
    key = "test.png"
    
    
    s3.Object('saltinedatabase', 'hello.txt').put(Body=open('/tmp/hello.txt', 'rb'))
    
    
    
    more_binary_data = b'Here we have some more data'
    bucket = 'saltinedatabase'
    key = 'test1.png'
    
    response = client.put_object(
        Body = more_binary_data, 
        Bucket = bucket, 
        Key = key)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda is working!!')
    }
