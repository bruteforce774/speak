#!/usr/bin/python3

import os
import json
from datetime import datetime, timedelta
import requests
import subprocess

CACHE_DIR = os.path.expanduser('~/.cache/weather')
CACHE_FILE = os.path.join(CACHE_DIR, 'forecast.json')
CACHE_HOURS = 6

LATITUDE = 59.91
LONGITUDE = 10.76

def get_greeting(name):
    current_hour = datetime.now().hour
    
    if current_hour >= 5 and current_hour < 12:
        time_of_day = "morning"
    elif current_hour >= 12 and current_hour < 18:
        time_of_day = "afternoon"
    elif current_hour >= 18 and current_hour < 22:
        time_of_day = "evening"
    else:
        time_of_day = "night"
    
    return f"Good {time_of_day}, {name}!"

def get_datetime_string():
    now = datetime.now()
    return now.strftime("%d %B %I:%M %p")

def is_cache_fresh():
    if not os.path.exists(CACHE_FILE):
        return False
    
    file_time = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
    time_difference = datetime.now() - file_time
    
    return time_difference < timedelta(hours=CACHE_HOURS)

def fetch_weather_from_api():
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    
    if not api_key:
        raise ValueError("OPENWEATHER_API_KEY environment variable not set")
    
    url = "https://api.openweathermap.org/data/3.0/onecall"
    params = {
        'lat': LATITUDE,
        'lon': LONGITUDE,
        'units': 'metric',
        'appid': api_key
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raises an error for bad status codes
    
    return response.json()

def save_cache(data):
    os.makedirs(CACHE_DIR, exist_ok=True)
    
    with open(CACHE_FILE, 'w') as f:
        json.dump(data, f)

def load_cache():
    with open(CACHE_FILE, 'r') as f:
        return json.load(f)
    
def get_weather_data():
    if is_cache_fresh():
        print("Using cached weather data")
        return load_cache()
    else:
        print("Fetching fresh weather data from API")
        data = fetch_weather_from_api()
        save_cache(data)
        return data
    
def get_today_weather_summary(weather_data):
    today = weather_data['daily'][0]
    
    temp_min = round(today['temp']['min'])
    temp_max = round(today['temp']['max'])
    description = today['weather'][0]['description']
    
    summary = f"Expect {description}, with a high of {temp_max}°C and a low of {temp_min}°C."
    
    return summary

def speak(message):
    try:
        subprocess.run(['spd-say', '-w', message], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error speaking: {e}")
    except FileNotFoundError:
        print("spd-say not found. Make sure speech-dispatcher is installed.")

def main():
    greeting = get_greeting("Daniel")
    date_time = get_datetime_string()
    weather = get_today_weather_summary(get_weather_data())
    
    message = f"{greeting} Today is {date_time}. {weather}"
    
    print(message)
    speak(message)

if __name__ == "__main__":
    main()