import requests
import json
import os
from datetime import datetime, timezone, timedelta

def get_weather_day(city, api_key):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        weather_description = data['weather'][0]['icon']
        temperature = data['main']['temp']

        return weather_description, temperature

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


def load_config():
    current_path = os.getcwd() 
    config_path = os.path.join(current_path, 'config.json')  
    with open(config_path) as file:
        config = json.load(file)
    API_KEY = config["Api_key"]["key"]
    return API_KEY

def load_all_weather_data(location):
    API_KEY = load_config()
    location_data = []

    for city in location:
        weather_description, temperature = get_weather_day(city, API_KEY)
        location_data.append({
        'city': city,
        'weather_description': weather_description,
        'temperature': temperature
    })
        
    return location_data

    

if __name__ == "__main__":
    """ load_weather_data("Oulu") """
    load_config()
