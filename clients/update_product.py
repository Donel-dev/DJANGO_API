import requests

endpoint = "http://localhost:8000/api/product/8/"

data = {
    'name': "PC_Gamer",
    'price': 3000000,
    'description': "electronique",
    'email' : "donel@example.com"
}

response = requests.put(endpoint, json=data)

print(response.json())
print(response.status_code)