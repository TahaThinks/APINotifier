import requests

iss_location = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=iss_location)

# Flag Errors in API for issues
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)