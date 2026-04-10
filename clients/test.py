import requests

endpoint = "http://localhost:8000/api/?q=Donelbukuto"

response = requests.get(endpoint)

print(response.json())
print(response.status_code)