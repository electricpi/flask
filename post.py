import requests

url = "http://localhost:8000/webhook"
data = {"key1": "value1"}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Content:", response.text)