import requests
from pprintpp import pprint

url = "https://reqres.in/api/users"
headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()

pprint(data)