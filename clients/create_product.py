import requests

endpoint = "http://localhost:8000/api/"

data = {
    'name': "Radio",
    'price': 25000, 
    'description':"electronique",
}

response = requests.post(endpoint, json=data)

print(response.json())
print(response.status_code)