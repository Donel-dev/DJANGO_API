import requests

endpoint = "http://localhost:8000/api/"

data = {
    'name': "PS5",
    'price': 200000, 
    'description':"electronique",
}

response = requests.get(endpoint)

print(response.json())
print(response.status_code)