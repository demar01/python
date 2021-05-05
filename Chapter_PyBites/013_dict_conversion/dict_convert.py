from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
Blog = namedtuple('Blog', blog.keys())

def dict2nt(dict_):
    # https://stackoverflow.com/questions/43921240/pythonic-way-to-convert-a-dictionary-into-namedtuple-or-another-hashable-dict-li
    return Blog(**dict_)


def nt2json(nt):
    #to encode json (serialization) use dumps (because we are not writing to disk)
    #see 2 namedtuple methods we need in here in this site https://docs.python.org/3/library/collections.html
    nt = nt._replace(started=str(nt.started))
    return json.dumps(nt._asdict())

#example _replace method for namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(11, y=22) 
# p._replace(x=33)
# p._asdict()


# A Simple Serialization Example
# data = {"president": {"name": "Zaphod Beeblebrox","species": "Betelgeusian"}}
# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)

# A Simple Deserialization Example
# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)
