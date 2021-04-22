
from pprint import pprint as pp
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_jeeps(cars=cars):
    """return a csved- str of Jeep models (original ordering)"""
    #return ", ".join(jeep for jeep in cars['Jeep'])
    return ", ".join(cars['Jeep'])

def get_first_value(cars=cars):
    """return a list of first models (original ordering)"""
    return [elem[0] for elem in cars.values()]


def get_Trail(cars=cars, search='trail'):
    """Return vehicles containing the string Trail in their names. sort the resulting sequence alphabetically"""
    return [model for models in cars.values() for model in models
            if search.lower() in model.lower()]


def sort_car_models(cars=cars):
    return {manufacturer:sorted(models) for manufacturer, models in cars.items()}
