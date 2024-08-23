import requests
response=requests.get("https://www.vedantu.com/home")
print(response.status_code)
if response.headers.get('Content-Type') == 'application/json':
    if response.text:
        print("Empty JSON response")
else:
    print("Response is not JSON")
    print(response.text)
    
    
# curl 'https://scheduling.vedantu.com/scheduling/session/getUserLatestActiveSessionFromCache?userId=5980003412213760&callingUserId=5980003412213760' \
#   -H 'accept: application/json, text/plain, */*' \
#   -H 'accept-language: en-US,en;q=0.9,te;q=0.8' \
#   -H 'cookie: _fbp=fb.1.1724335335205.532445085510795748; _ga=GA1.1.165265297.1724335336; v-auth-token=8HQ63zA7QqVd8mMu; auth-token=8Hq63zA7QqVd8mMU; _gcl_au=1.1.1952375409.1724335335.715269045.1724335343.1724335358; X-Ved-Token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbi5tYW5pc2hAdmVkYW50dS5jb20iLCJleHAiOjE3Mjk1MTkzNTgsImlzcyI6InZlZGFudHUuY29tIiwic2Vzc2lvbkRhdGEiOiJ7XCJmaXJzdE5hbWVcIjpcIk1hbmlzaFwiLFwibGFzdE5hbWVcIjpcIlNpbmdoXCIsXCJmdWxsTmFtZVwiOlwiTWFuaXNoIFNpbmdoXCIsXCJ1c2VySWRcIjo1OTgwMDAzNDEyMjEzNzYwLFwiY2hpbGRyZW5Vc2VySWRzXCI6W10sXCJlbWFpbFwiOlwiYWRtaW4ubWFuaXNoQHZlZGFudHUuY29tXCIsXCJwcm9maWxlUGljVXJsXCI6XCJodHRwczovL3ZlZGFudHUtcHJvZmlsZS1waWNzLnMzLmFwLXNvdXRoLTEuYW1hem9uYXdzLmNvbS9QUk9ELzA4ZjMxMzVhLWI1NGUtNDY2Yy05ZTkwLTljYzI5NzdiNmE5NS0xNjEzMzg1MTcxOTAzLTQ5YzU0ZmUzLWZiNGQtNDhmZS05ZjY5LTdkNjkzZTdmMjA3MS5wbmdcIixcInJvbGVcIjpcIlNUVURFTlRcIixcImNvbnRhY3ROdW1iZXJcIjpcIjI3MDAzNzgzXCIsXCJwaG9uZUNvZGVcIjpcIjkxXCIsXCJjcmVhdGlvblRpbWVcIjoxNzI0MzM1MzU4OTYzLFwiZXhwaXJ5VGltZVwiOjE3Mjk1MTkzNTg5NjMsXCJpc0VtYWlsVmVyaWZpZWRcIjp0cnVlLFwiaXNDb250YWN0TnVtYmVyVmVyaWZpZWRcIjp0cnVlLFwiaXNDb250YWN0TnVtYmVyRE5EXCI6ZmFsc2UsXCJpc0NvbnRhY3ROdW1iZXJXaGl0ZWxpc3RlZFwiOmZhbHNlLFwicmVmZXJyYWxDb2RlXCI6XCJtYW5pMzM4ZlwiLFwidG5jVmVyc2lvblwiOlwidjlcIixcImRldmljZVwiOlwiV0VCXCIsXCJncmFkZVwiOlwiMTNcIixcInBhc3N3b3JkQXV0b2dlbmVyYXRlZFwiOmZhbHNlLFwiYm9hcmRcIjpcInN0YXRlIGJvYXJkXCIsXCJleGFtVGFyZ2V0c1wiOltcIk5FRVRcIixcIkpFRVwiLFwiZW5nbGlzaCBwcm9cIl0sXCJ1c2VySW5Qcm9jZXNzT2ZPbmJvYXJkaW5nXCI6ZmFsc2UsXCJ0YXJnZXRcIjpcIk5FRVRcIixcInN0dWRlbnRJbmZvXCI6e1wiZXhhbVRhcmdldHNcIjpbXSxcInBhcmVudEluZm9zXCI6W3tcInR5cGVcIjpcIkZBVEhFUlwiLFwiZmlyc3ROYW1lXCI6XCJzZGZkXCIsXCJsYXN0TmFtZVwiOlwic2Rmc2RmXCIsXCJlbWFpbFwiOlwic2Zmc0B2ZWRhbnR1LmNvbVwiLFwiZW1haWxWZXJpZmllZFwiOmZhbHNlLFwiY29udGFjdE51bWJlclwiOlwiMTIzMTIzMTIzMVwiLFwicGhvbmVDb2RlXCI6XCI5MVwiLFwiY29udGFjdE51bWJlclZlcmlmaWVkXCI6ZmFsc2UsXCJwcmltYXJ5Q29udGFjdFBlcnNvblwiOmZhbHNlLFwid2hhdHNBcHBQaG9uZVZlcmlmaWVkXCI6ZmFsc2V9XSxcInVwZGF0ZU5lZWRlZFwiOmZhbHNlfSxcImxhbmd1YWdlUHJlZnNWMlwiOltcIkVuZ2xpc2ggTWVkaXVtXCJdLFwiZ2VuZGVyXCI6XCJNQUxFXCIsXCJpc0F1cm9TY2hvbGFyVXNlclwiOmZhbHNlfSJ9.ClhAj_GI8O6wi-6vW5bK1JPCoNBUL4hTO1gnvI05ki3cBntXpejRMpJbp8FH1VU7-b1NEV1hIHMrbzCSWXO7oA; USE_APP_AB=VARIANT2; _uetsid=2335c290608f11efadcab7eaa3424f25; _uetvid=23360930608f11efb183b7efb280d30c; moe_uuid=59a4d037-7728-4a70-8664-e3c0f2429d8f; _clck=qp80qn%7C2%7Cfoj%7C0%7C1695; _clsk=zbla72%7C1724335363239%7C1%7C1%7Cv.clarity.ms%2Fcollect; USER_DATA=%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A5980003412213760%2C%22updated_at%22%3A1724335364237%7D%2C%7B%22key%22%3A%22USER_ATTRIBUTE_USER_MOBILE%22%2C%22value%22%3A%229127003783%22%2C%22updated_at%22%3A1724335364883%7D%2C%7B%22key%22%3A%22USER_ATTRIBUTE_USER_EMAIL%22%2C%22value%22%3A%22admin.manish%40vedantu.com%22%2C%22updated_at%22%3A1724335365183%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2259a4d037-7728-4a70-8664-e3c0f2429d8f%22%2C%22deviceAdded%22%3Atrue%7D; SESSION=%7B%22sessionKey%22%3A%22f3ffe2e7-fd77-4ceb-8c6b-01f42588df3f%22%2C%22sessionStartTime%22%3A%222024-08-22T14%3A02%3A44.239Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1724337169685%2C%22numberOfSessions%22%3A1%7D; _ga_35N6JBZRVC=GS1.1.1724335335.1.1.1724335370.25.0.0' \
#   -H 'origin: https://www.vedantu.com' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.vedantu.com/home' \
#   -H 'sec-ch-ua: "Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"' \
#   -H 'sec-ch-ua-mobile: ?1' \
#   -H 'sec-ch-ua-platform: "Android"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36'