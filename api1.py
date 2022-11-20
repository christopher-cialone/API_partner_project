import requests
import json


user_input = input("What is your name?: ")

url = “https://api.agify.io/?name=" + user_input

result = requests.get(url)
name = json.loads(result.text)
#print(name)
#print(type(name))
#print(result.text)
name_age_generator = f’Hello {name[“name”]} your real age is {name[“age”]}, be happy '
print(name_age_generator)