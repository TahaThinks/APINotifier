import requests

iss_location = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=iss_location)

# Check Errors in API
if response.status_code == 404:
    raise Exception("That resource does not exist.")
elif response.status_code == 401:
    raise Exception("You are not Authorized")


