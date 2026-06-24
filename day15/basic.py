import requests

response = requests.get("https://httpbingo.org/get")

print("status code:",response.status_code)
print("Headers : ",response.headers["Content-Type"])
print("Body (raw text):", response.text[100])
if response.status_code == 200:
    print("Body(parsed JSON)",response.json())
else:
    print("Server returned an error, no Json to parse.")
