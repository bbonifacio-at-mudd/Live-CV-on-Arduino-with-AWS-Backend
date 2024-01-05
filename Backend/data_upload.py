import requests
import base64
import json

# The URL of the API Gateway endpoint
api_url = 'https://your-api-gateway-url'

# The path to the image on your local filesystem
image_path = '/path/to/image.png'

# The metadata dictionary
metadata = {'name': 'image.png', 'label': 'label'}

# Read the image data and encode it in base64
with open(image_path, 'rb') as image_file:
    encoded_image_data = base64.b64encode(image_file.read())

# Structure the payload
payload = {
    'image_data': encoded_image_data.decode('utf-8'),  # Lambda expects a base64-encoded string
    'metadata': metadata
}

# Make the POST request to the API Gateway
response = requests.post(api_url, data=json.dumps(payload))

# Print out the response
print(response.text)
