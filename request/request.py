import requests

url = "https://scheduling.vedantu.com/scheduling/session/getUserLatestActiveSessionFromCache?userId=5980003412213760&callingUserId=5980003412213760"

response = requests.get(url)

if response.headers.get("Content-Type") == "application/json":
    try:
        print(response.json())
    except ValueError:
        print("Error parsing JSON response")
else:
    print("Response is not in JSON format:")
    print(response.text)
