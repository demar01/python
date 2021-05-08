cars=[{"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},\
    {"id":2,"automaker":"Chrysler","model":"Town & Country","year":1999},\
        {"id":3,"automaker":"Porsche","model":"Cayenne","year":1999},\
            {"id":4,"automaker":"Dodge","model":"Ram Wagon B350","year":1999},
            {"id":1,"automaker":"Chrysler","model":"Ram Van 1500","year":2000},\
    {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2000},\
        {"id":3,"automaker":"Porsche","model":"Cayenne","year":2000},\
            {"id":4,"automaker":"Dodge","model":"Ram Wagon B350","year":2000}]

import requests

# r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
# r # <Response [200]>; dir(r); type(r)  <class 'requests.models.Response'>

CARS = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

with requests.Session() as s:
    data = s.get(CARS).json()


from collections import Counter

def automaker_year(year):
    cars_year = [car['automaker'] for car in data if car["year"] == year]
    return cars_year

def most_prolific_automaker(year):
     cars_year = [car['automaker'] for car in data if car["year"] == year]
     return Counter(cars_year).most_common(1)[0][0]

def get_models(automaker, year):
    return set([car['model'] for car in data if car["year"] == year and car["automaker"] == automaker])
#in the test file there is a hint that this function should return a set. Sets do faster look up than dictionaries.

