import requests
import os
from dotenv import load_dotenv

load_dotenv() # by default read env from .env file
api_key = os.getenv("OPENWEATHER_API_KEY")
city = input("Enter city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
response = requests.get(url)
weather = response.json()
print(weather)

