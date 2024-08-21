from dotenv import load_dotenv
import os
import requests

# - - - - - - - - - - - - Pulling API info - - - - - - - - - - - - #

load_dotenv()
# Replace with your actual latitude, longitude, and API key
lat = "25.7617"
lon = "-80.1918"
weather_api_key = os.getenv("WEATHER_API_KEY")

# Construct the full URL
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}"
# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)  # You can access specific data like data['weather'], data['main'], etc.
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    print(f"Temperature: {temperature}K")
    print(f"Weather: {weather_description}")
else:
    print(f"Error: {response.status_code}")
