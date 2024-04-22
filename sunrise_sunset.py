import requests

MY_LAT = 25.204849
MY_LON = 55.270782

sunset_sunrise_url = "https://api.sunrise-sunset.org/json"
my_parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
}
response = requests.get(url=sunset_sunrise_url, params=my_parameters)

# Raise if issues
response.raise_for_status()

# Check Status Code
print(response.status_code)

# Get the Data
data = response.json()["results"]

sunrise = data["sunrise"]
sunset = data["sunset"]

print(data)
