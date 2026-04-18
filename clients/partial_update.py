import requests

endpoint = "http://localhost:8000/api/product/8/"

data = {
    'price': 2200000,
}

response = requests.patch(endpoint, json=data)

print(response.json())
print(response.status_code)