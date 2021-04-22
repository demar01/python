import pytest

from cars import get_first_value, get_jeeps,cars

def test_get_jeeps():
    assert get_jeeps()=='Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    assert type(get_first_value())== str

def test_first_cars():
    assert get_first_value()==['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    assert type(get_first_value())== list


def test_sort_dict_alphabetically():
    actual = sort_car_models()
    # Order of keys should not matter, two dicts are equal if they have the
    # same keys and the same values.
    # The car models (values) need to be sorted here though
    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }
    assert actual == expected
