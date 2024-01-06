import json
import base64
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    http_method = event['requestContext']['http']['method']
    
    if http_method == "POST":
        try:
            bucket = "saltinedatabase"
            body = event['body']
            body_decoded = base64.b64decode(body)
            body_string = body_decoded.decode('utf-8')
            body_dict = json.loads(body_string)

            image_data = base64.b64decode(body_dict['image_data'])
            metadata = body_dict['metadata']
            key = metadata['name']

            # Ensure the file is a PNG
            if not key.lower().endswith('.png'):
                return {
                    'statusCode': 400,
                    'body': json.dumps("The file is not a PNG image.")
                }

            content_type = metadata.get('Content-Type', 'image/png')

            # Determine the directory based on the label
            label = metadata.get('label', '').lower()
            if label not in ['whole', 'broken']:
                return {
                    'statusCode': 400,
                    'body': json.dumps("Invalid label. Must be 'whole' or 'broken'.")
                }

            directory = f"liveImages/{label}/"
            s3_key = f"{directory}{key}"

            # Check if the image already exists
            try:
                response = s3_client.head_object(Bucket=bucket, Key=s3_key)
                # If the above line does not raise an error, the object exists
                return {
                    'statusCode': 500,
                    'body': json.dumps(f"This image already exists in the database: {s3_key}")
                }
            except ClientError as e:
                if e.response['Error']['Code'] == '404':
                    # Object does not exist, so proceed to upload
                    response = s3_client.put_object(
                        Body=image_data, 
                        Bucket=bucket,
                        Key=s3_key,
                        ContentType=content_type  # Set the content type
                    )
                    return {
                        'statusCode': 200, 
                        'body': json.dumps(f'Image Posted Successfully: {s3_key}')
                    }
                else:
                    # Reraise the exception if it's not a '404' error
                    raise e
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Failed in Lambda Post: {str(e)}')
            }
