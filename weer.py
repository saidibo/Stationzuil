import requests

# import request
def rek_api():
    resource_uri = "https://api.openweathermap.org/data/2.5/weather?q=amsterdam&appid=623674843eb5b413c214a36bad8eefdc"
    response = requests.get(resource_uri)
    response_data = response.json()
    weer = response_data['main']
    celcius = round(float(weer['temp'] - 273),2)
    return str(celcius) + '°C'

def rek_icon():
    resource_uri = "https://api.openweathermap.org/data/2.5/weather?q=amsterdam&appid=623674843eb5b413c214a36bad8eefdc"
    response = requests.get(resource_uri)
    response_data = response.json()
    weer = ((response_data['weather'])[0])
    return weer['icon']



if __name__ == "__main__":
    rek_api()