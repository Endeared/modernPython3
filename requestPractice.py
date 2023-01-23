import requests

url = "http://www.google.com"
response = requests.get(url)

print(f'Your request to {url} came back with code {response.status_code}!')
print(response.text)