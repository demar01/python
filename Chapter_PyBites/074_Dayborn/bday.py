import calendar 


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    day = date.weekday() #This returns an int. So Monday is 0. 
    return calendar.day_name[day] #This returns the string week name . So if day is 0 , it will return Monday


day=date(1974, 11, 11).weekday()

#  weekday_of_birth_date(date(1974, 11, 11))