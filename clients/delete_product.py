import requests

endpoint = "http://localhost:8000/api/product/18/"

response = requests.delete(endpoint)

print(response.json())
print(response.status_code)