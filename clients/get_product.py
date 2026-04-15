import requests

endpoint = "http://localhost:8000/api/product/8/"

data = {
    'name': "Television",
    'price': 250000,
    'description': "electronique",
    'email' : "donel@example.com"
}

response = requests.get(endpoint)

print(response.json())
print(response.status_code)