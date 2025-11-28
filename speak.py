#!/usr/bin/python3

from datetime import datetime

def get_greeting(name):
    current_hour = datetime.now().hour
    
    # TODO: Add conditional logic here
    # What comparison operators do we need?
    # Hint: We need to check if current_hour falls within ranges
    
    if current_hour >= 5 and current_hour < 12:
        time_of_day = "morning"
    # ... what comes next?
    
    return f"Good {time_of_day}, {name}!"

# Test it
print(get_greeting("Daniel"))