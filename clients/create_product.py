import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    'name': "Television",
    'price': 250000,
    'description': "electronique"
}

response = requests.post(endpoint, json=data)

print(response.json())
print(response.status_code)