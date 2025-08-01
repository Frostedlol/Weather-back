import requests
import json
import os

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
        weather_description = data['weather'][0]['description']
        return city_name, temperature, weather_description
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

    except KeyError:
        print("Error: Unable to parse weather data. Check the city name or API key.")

""" with open('config.json', "r") as file:
    config = json.load(file)

print(config) """
Location = "Oulu"
base_dir = os.path.dirname(os.path.abspath(__file__))
print(base_dir)

# Fetch weather for Oulu
""" name, temp, weather_desc = get_weather("Location", API_KEY)

if name and temp and weather_desc:
    print(f"Weather in {name}: {temp}°C, {weather_desc}") """