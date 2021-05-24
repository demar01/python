import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    pattern = r"INFO \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2} Shutdown initiated."
    if re.match(pattern, text):
        return True

# has_timestamp('INFO 2014-07-03T23:27:51 Shutdown initiated.')

def is_integer(number):
    """Return True if number is an integer"""
    pattern = r"^-?\d+$"
    if re.match(pattern, str(number)):
        return True

# is_integer(1)