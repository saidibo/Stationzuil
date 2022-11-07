import requests
import gs
# import request
def rek_api():
    resource_uri = f"https://api.openweathermap.org/data/2.5/weather?q=amsterdam&appid=28d6e5af678b6c23a3752ff387b58633"
    response = requests.get(resource_uri)
    response_data = response.json()
    weer = response_data['main']
    celcius = round(float(weer['temp'] - 273),2)
    return str(celcius) + '°C'

def rek_icon():
    resource_uri = f"https://api.openweathermap.org/data/2.5/weather?q=amsterdam&appid=28d6e5af678b6c23a3752ff387b58633"
    response = requests.get(resource_uri)
    response_data = response.json()
    weer = ((response_data['weather'])[0])
    return weer['icon']

