import requests
from datetime import datetime

MY_LAT = 25.276987
MY_LON = 55.296249
FORMAT = 0
TIMEZONE = "Asia/Muscat"

sunset_sunrise_url = "https://api.sunrise-sunset.org/json"
my_parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": FORMAT,
    "tzid": TIMEZONE
}
response = requests.get(url=sunset_sunrise_url, params=my_parameters)

# Raise if issues
response.raise_for_status()

# Check Status Code
# print(response.status_code)

# Get the Data
data = response.json()["results"]

sunrise = data["sunrise"]
sunset = data["sunset"]

print(f"sunrise: {sunrise}\nsunset: {sunset}")

time_now = datetime.now()
print(time_now)
