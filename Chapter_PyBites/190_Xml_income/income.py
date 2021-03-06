import os
from pathlib import Path
from urllib.request import urlretrieve
from collections import defaultdict
import xml.etree.ElementTree as etree

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


def _get_root(xml):
    return etree.parse(xml).getroot() #this will return <Element '{http://www.worldbank.org}countries' at 0x1185b7b30>


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
    - keys = incomes (wb:incomeLevel)
    - values = list of country names (wb:name)
    """
    income_distribution = defaultdict(list) # we will append info to here 
    root = _get_root(xml)
    for child in root:
        country_name = child.findtext('{http://www.worldbank.org}name') #countries names
        income_level = child.findtext('{http://www.worldbank.org}incomeLevel')
        income_distribution[income_level].append(country_name) #stadard way of appending to a default dict. 
    return income_distribution #default dictionary sorted nby income level