import requests

# The URL of the API Gateway endpoint for the GET request
api_url = 'https://your-api-gateway-url/resource-path'

# Make the GET request to the API Gateway
response = requests.get(api_url)

# Print out the response
print(response.text)
