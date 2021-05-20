# Bite 219. Bite notification planner

## Description

Another real world use case. When we added notifications to our learning paths, we gave the user the option to receive x number of Bites every y number of days. Based on these two input parameters, code up the gen_bite_planning generator that returns date objects for the notifications.

With the default set to notify one Bite a day, the script using your gen_bite_planning generator would output the following:

>>> from datetime import date
>>> from notifications import gen_bite_planning
>>> today = date.today()
>>> today
datetime.date(2019, 8, 25)
>>> gen = gen_bite_planning(num_bites=1, num_days=1, start_date=today)
>>> for _ in range(10):
...     next(gen)
...
datetime.date(2019, 8, 26)
datetime.date(2019, 8, 27)
datetime.date(2019, 8, 28)
datetime.date(2019, 8, 29)
datetime.date(2019, 8, 30)
datetime.date(2019, 8, 31)
datetime.date(2019, 9, 1)
datetime.date(2019, 9, 2)
datetime.date(2019, 9, 3)
datetime.date(2019, 9, 4)

If the user decides to do 2 Bites every 3 days, the generator would output the following:

>>> gen = gen_bite_planning(num_bites=2, num_days=3, start_date=today)
>>> for _ in range(10):
...     next(gen)
...
datetime.date(2019, 8, 28)
datetime.date(2019, 8, 28)
datetime.date(2019, 8, 31)
datetime.date(2019, 8, 31)
datetime.date(2019, 9, 3)
datetime.date(2019, 9, 3)
datetime.date(2019, 9, 6)
datetime.date(2019, 9, 6)
datetime.date(2019, 9, 9)
datetime.date(2019, 9, 9)