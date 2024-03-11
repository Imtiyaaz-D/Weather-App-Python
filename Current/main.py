import datetime as dt
import requests

BASE_URL = "http:api.openweathermap.org/data/3.0/weather?"
API_KEY = "b4545f98b2f26ca3164615d436f6ebb2"
CITY = "Cape Town"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)