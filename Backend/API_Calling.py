import requests
import json
import base64
import os

api_invoke_url = "https://s0d1lij4o8.execute-api.us-east-1.amazonaws.com/beta/dataController"

image_path = r"C:\Users\Brandon\Desktop\Projects\Live-CV-on-Arduino\Backend\Example_files\image_20231227_102410.png"

# Ensure the file is a PNG
if not image_path.lower().endswith('.png'):
    raise ValueError("The file is not a PNG image.")

metadata = {'name': os.path.basename(image_path), 'label': 'whole', 'Content-Type': 'image/png'}

with open(image_path, 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

data = {
    'image_data': encoded_string,
    'metadata': metadata
}

response = requests.post(api_invoke_url, data=json.dumps(data))

print(response.text)
print(response.status_code)
