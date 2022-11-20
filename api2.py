import requests
import json
"""
New York:
Latitude:  40.7127281
Longitued:  -74.0060152
"""

user_input = input("Enter a city to get weather info: ") 
# this api call will get us the Latitude and Longitued
BASE_URL = 'http://api.openweathermap.org/geo/1.0/direct?'
API_KEY = open('api.txt', 'r').read()
CITY = user_input

url = BASE_URL + "q=" + CITY + "&appid=" + API_KEY # Makes up the first API call
result = requests.get(url)

# Parse the result using json which converts it to a python object
weather = json.loads(result.text) # python list [{'lat':randomnumber,'lon':randomnumber}]
# print(type(weather))
# print("Latitude: " ,new_york_weather[0]['lat'])
# print("Longitued: ",new_york_weather[0]['lon'])



######################################################################################################################
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
LAT = weather[0]['lat']
LON = weather[0]['lon']

url = f"{BASE_URL}lat={LAT}&lon={LON}&appid={API_KEY}" # Makes up Second API Call
# print(url)
result = requests.get(url)
weather = json.loads(result.text) # from json to a python object 

print(user_input)
for key,value in weather['main'].items():
    print(f"{key} : {value}")





