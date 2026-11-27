#Validate a real API response using Pydantic

import requests
from pydantic import BaseModel,Field,ValidationError

class Weather(BaseModel):
    latitude : float
    longitude : float
    current : dict

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 11.0168,
    "longitude": 76.9558,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

try:
    response = requests.get(url,params=params,timeout =10)
    response.raise_for_status()
    
    data = response.json()
    
    """response by api of raw data
    print(data)"""
    
    #check api error
    if data.get("error"):
        raise ValueError(data.get("reason","unknown Api error"))
    
    """removing the longitude before validation
    data.pop("longitude")"""
    
    #validate
    weather = Weather.model_validate(data)
    
    #display
    print("\n===========Weather Report===========")
    print(weather.latitude)
    print(weather.longitude)
    print("Temp: ",weather.current["temperature_2m"],"C")
    print("Humidity: ",weather.current["relative_humidity_2m"],"%")
    print("Wind Speed:",weather.current["wind_speed_10m"], "km/h")    
    print("======================================")
    
except requests.RequestException as e:
    print("Api connection error: ",e)
    
except ValueError as e:
    print("Api error: ", e)
    
except ValidationError as e:
    print("Error: ",e)