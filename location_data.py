from dotenv import load_dotenv
import os
import requests

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")
limit = 5

# The info will be imported from the main file and used here to fetch the api info
info = "temp"
url = f"http://api.openweathermap.org/geo/1.0/direct?q={info}&limit={limit}&appid={weather_api_key}"