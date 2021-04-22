from datetime import datetime
from datetime import timedelta
from pprint import pprint as pp
from itertools import islice


PYBITES_BORN = datetime(year=2016, month=12, day=19)
hundred_days = timedelta(days=100)
one_year = timedelta(days=365)


def gen_special_pybites_dates():
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)


gen = gen_special_pybites_dates()
dates = list(islice(gen, 5))
pp(dates)