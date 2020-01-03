import requests
import json
import re
import math
# from urllib import urlopen

def catFact():
    data = requests.get('https://catfact.ninja/fact')
    return (data.json()['fact'])

def jokes():
    data = requests.get('https://icanhazdadjoke.com/slack')
    return (data.json()['attachments'][0]['text'])

def location():
    response = requests.get('http://ipinfo.io/json')
    data = response.json()

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    loc = data['loc']

    # print('Your IP detail\n ')
    # print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))
    return loc

def getWeather():
    city_coord = location()
    city_coord = city_coord.split(',')
    # print(city_coord)
    city_lat = city_coord[0]
    city_long = city_coord[1]
    # print(city_lat, city_long)
    data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?APPID=c1ba74c1bc8ebe7734a3a8070b0be516&lat={city_lat}&lon={city_long}')
    def convertToCelsius(kelvin):
        temp_in_celsius = int(kelvin)-275
    weather_descr = data.json()['weather'][0]['description']
    weather_temp = data.json()['main']['temp']
    weather_name = data.json()['name']
    response = f'the current weather in {weather_name} is {weather_descr} with a temperature of {weather_temp}'
    return response
