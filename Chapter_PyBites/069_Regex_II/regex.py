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

def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    pattern = r"\S-\S"
    if re.search(pattern, text):
        return True

def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    pattern = r"\s?\(.*?\)" #will match parenthesis, whatever is inside them and any previous whitespace
    return re.sub(pattern, "", text)


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    pattern = r"\s{2,}"
    return re.sub(pattern, " ", text)



# re.search("^The.*Spain$","The rain in Spain") 
# . Any character (except newline character) 
# * Zero or more occurrences
# re.findall("ai", "The rain in Spain")
# re.findall("Portugal","The rain in Spain")
# print("The first white-space character is located in position:", re.search("\s", "The rain in Spain").start())

#re.sub(' {2,}', ' ', 'The     quick brown    fox')