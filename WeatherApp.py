# weather application

import os
import requests
from dotenv import load_dotenv

load_dotenv()

CITY = os.getenv("CITY", "chennai")
LATITUDE = float(os.getenv("LATITUDE", 13.0827))
LONGITUDE = float(os.getenv("LONGITUDE", 80.2707))

def get_weather():
    
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude":LATITUDE,
        "longitude":LONGITUDE,
        "current":[
            "temperature_2m",
            "wind_speed_10m",
            "weather_code",
            "relative_humidity_2m"
        ],
        "timezone":"auto"
    }
    
    try:
        response = requests.get(
            url, 
            params=params,
            timeout = 10
        )
        
        response.raise_for_status()
        #print(response.text)
        data = response.json()
        return data["current"]
        
    except requests.exceptions.Timeout:
        print("Timeout")
        
    except requests.exceptions.HTTPError as error:
        print("HTTP Error:", error)
        
    except requests.exceptions.RequestException as error:
        print("Network error:", error)
        
    except (ValueError, NameError, KeyError) as error:
        print("Invalid Response:", error)
        
    return None
    
def display_weather(weather):
    
    if weather is None:
        return
    
    print("\n=====Weather Report=====")
    
    print("Location: ", CITY)
    print("Temperature: ", weather["temperature_2m"], "C")
    print("Humidity: ", weather["relative_humidity_2m"], "%")
    print("Wind Speed: ", weather["wind_speed_10m"], "km/hr")
    print("Weather code: ", weather["weather_code"])
    
    print("========================")
    
def main():
    
    print("Fetching weather data")
    weather = get_weather()
    display_weather(weather)
    
if __name__ == "__main__":
    main()