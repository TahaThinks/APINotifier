import requests

iss_location = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=iss_location)

# Flag Errors in API for issues
response.raise_for_status()

data = response.json()["iss_position"]
print(data)