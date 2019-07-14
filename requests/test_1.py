import requests

url = "http://localhost"
r = requests.get(url)
print(r.headers)