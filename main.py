# working with apis and dictionaries
import requests
import json
response= requests.get("https://randomuser.me/api")
#print(response.json())

title= response.json()['results'][0]['name']['first']
print(title)
gender= response.json()['results'][0]['gender']
print(gender)
last= response.json()['results'][0]['name']['last']
print(last)
street= response.json()['results'][0]['location']['street']['name']
print(street)
city= response.json()['results'][0]['location']['city']
print(city)
state= response.json()['results'][0]['location']['state']
print(state)
country= response.json()['results'][0]['location']['country']
print(country)
postcode=response.json()['results'][0]['location']['postcode']
print(postcode)


