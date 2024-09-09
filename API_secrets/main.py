import requests
import os

api_url = "https://example.com/api/get-token"
api_key = "your_api_key_here" 
response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})
if response.status_code == 200:
    token = response.json().get("token")
    if token:
        os.environ["SECRET_TOKEN"] = token
        print("Token retrieved and set as environment variable.")
    else:
        print("Token not found in the response.")
else:
    print(f"Failed to retrieve token. Status code: {response.status_code}")
    print("Response:", response.text)
