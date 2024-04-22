import requests

sunset_sunrise_url = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat": 25.204849,
    "lon": 55.270782,
}
response = requests.get(url=sunset_sunrise_url)

# Raise if issues
response.raise_for_status()