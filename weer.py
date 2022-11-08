import requests
"""
import request
"""

""""
api call voor de steden die ik heb in tkinter scherm, hier word kelvin naaf graden berekent.
"""
def rek_api(city):
    resource_uri = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=28d6e5af678b6c23a3752ff387b58633"
    response = requests.get(resource_uri)
    response_data = response.json()
    weer = response_data['main']
    celcius = round(float(weer['temp'] - 273),2)
    return str(celcius) + '°C'

""""
api call voor de ICONS in de tkinter scherm per stad.
"""
def rek_icon(city):
    resource_uri = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=28d6e5af678b6c23a3752ff387b58633"
    response = requests.get(resource_uri)
    response_data = response.json()
    weer = ((response_data['weather'])[0])
    return weer['icon']

