#!/usr/bin/python3

import os
import json
from datetime import datetime, timedelta
import requests

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
    """Check if cache file exists and is less than CACHE_HOURS old"""
    if not os.path.exists(CACHE_FILE):
        return False
    
    # Get file modification time
    file_time = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
    time_difference = datetime.now() - file_time
    
    return time_difference < timedelta(hours=CACHE_HOURS)

def main():
    greeting = get_greeting("Daniel")
    date_time = get_datetime_string()
    message = f"{greeting} Today is {date_time}."
    
    print(message)

if __name__ == "__main__":
    main()