import requests
import json
import os
from datetime import datetime, timezone, timedelta

def get_weather(city, api_key):
    # OpenWeather API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Make a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the JSON response
        data = response.json()

        # Extract relevant weather information
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['icon']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        return city_name, temperature, weather_description, humidity, wind_speed, sunrise, sunset
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

def get_weather_day(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        timetemp = []
        timetemp_week = []

        today = datetime.now()
        formatted_date = today.strftime("20%y-%m-%d")
        midnight_time = (today + timedelta(days=1)).strftime("20%y-%m-%d 00:00:00")


        for item in data['list']:
            timestamp = item['dt_txt']
            temperature = item['main']['temp']
            feels_like = item['main']['feels_like']
            humidity = item['main']['humidity']
            weather_description = item['weather'][0]['icon']  
            rain_probability = round(item["pop"] * 100)

            timetemp_week.append({
                'timestamp': timestamp,
                'temperature': temperature,
                'weather_description': weather_description,
                'feels_like': feels_like,
                'humidity': humidity,
                'rain_probability': rain_probability
            })

            if formatted_date not in item['dt_txt'] and midnight_time not in item['dt_txt']:
                continue
        
            timetemp.append({
                'timestamp': timestamp,
                'temperature': temperature,
                'weather_description': weather_description,
                'feels_like': feels_like,
                'humidity': humidity
            })


        return timetemp, timetemp_week
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


def load_config():
    current_path = os.getcwd() 
    config_path = os.path.join(current_path, 'config.json')  # Construct the path to config.json
    with open(config_path) as file:
        config = json.load(file)
    API_KEY = config["Api_key"]["key"]
    return API_KEY

def load_weather_data(location):
    API_KEY = load_config()
    name, temp, weather_desc, humidity, windspeed, sunrise, sunset = get_weather(location, API_KEY)
    todays_weather, week_weather = get_weather_day(location, API_KEY)

    # Convert sunrise and sunset from Unix timestamp to local time
    if sunrise and sunset:
        sunrise = datetime.fromtimestamp(sunrise, timezone.utc).astimezone().strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(sunset, timezone.utc).astimezone().strftime('%H:%M:%S')


    if name and temp and weather_desc:
        location_data = {
            "name": name,
            "temperature": temp,
            "weather_description": weather_desc,
            "humidity": humidity,
            "wind_speed": windspeed,
            "sunrise": sunrise,
            "sunset": sunset
        }
        
        return location_data, todays_weather, week_weather

    

if __name__ == "__main__":
    """ load_weather_data("Oulu") """
    load_config()
