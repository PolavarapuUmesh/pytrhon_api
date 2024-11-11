# import requests

# url="https://subscription.vedantu.com/subscription/bundle/getActiveEnrol"
# response = requests.get(url)

# if response.headers.get("Content-Type") == "application/json":
#     try:
#         print(response.json())
#     except ValueError:
#         print("Error parsing JSON response")
# else:
#     print("Response is not in JSON format:")
#     print(response.text)


import requests
import json

# url="https://user.vedantu.com/user/getUserProfile?userId=410262624268"
# url="https://subscription.vedantu.com/subscription/bundle/microcourse/v1/popular-for-home-feed?grade=13"
url="http://127.0.0.1:8000/docs#/"
response = requests.get(url)
if response.headers.get("Content-Type") == "application/json":
    try:
            print(response.json())
    except ValueError:
        print("Error parsing JSON response")
else:
    print("Response is not in JSON format:")
print(response.text)
