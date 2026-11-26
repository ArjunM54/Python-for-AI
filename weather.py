import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 13.0827,
    "longitude": 80.2707,
    "current": "temperature_2m"
}

response = requests.get(url, params=params)

#print(response) gives the status code.
#print(response.text) displays the text about the parameters
#print(type(response)) display the type of response

data = response.json() #its like the json.dump method.which means json object to python dict.

print(type(data))
print(data["current"]["temperature_2m"])