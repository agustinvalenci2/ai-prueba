import requests
import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/"


def get_weather(city: str):
    """Obtiene el clima actual de una ciudad usando OpenWeather API"""
    API_KEY = OPENWEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"El clima en {city} es {data['weather'][0]['description']} con {data['main']['temp']}°C."
    return f"No se pudo obtener el clima para {city}."




