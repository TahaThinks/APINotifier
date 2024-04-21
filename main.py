import requests

iss_location = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=iss_location)
print(response)

