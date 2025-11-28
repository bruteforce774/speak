#!/usr/bin/python3

from datetime import datetime

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

print(get_greeting("Daniel"))

def get_datetime_string():
    now = datetime.now()
    return now.strftime("%d %B %I:%M %p")

date_time = get_datetime_string()
print(date_time)