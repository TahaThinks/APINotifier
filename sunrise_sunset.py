import requests

sunset_sunrise_url = "https://api.sunrise-sunset.org/json"
response = requests.get(url=sunset_sunrise_url)

# Raise if issues
response.raise_for_status()