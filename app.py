import requests
import config
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer "+config.api
}
params = {
    "term": "barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
x = response.json()["businesses"]
y = [i["name"] for i in x if i["rating"] == 5.0]
for i in y:
    print(i, end="\n\n")
