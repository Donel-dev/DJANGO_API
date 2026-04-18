import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    'name': "Server",
    'price': 300000,
    'description': "electronique",
    'email' : "donel@example.com"
}

response = requests.post(endpoint, json=data)

print(response.json())
print(response.status_code)