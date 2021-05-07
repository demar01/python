import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, "r") as f:
        word = f.read().splitlines() 
    return word

def calc_word_value(words=load_words()):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    # get() method returns the value for the specified key if key is in dictionary
    # d.get(key,default). So the 0 is to return 0 instead of none when not found. 
    return sum([LETTER_SCORES.get(word.upper()) for word in words])

def max_word_value(words='bob', 'julian', 'pybites', 'quit', 'barbeque']):
    """Given a list of words calculate the word with the maximum value and return it"""
    return max(testwords, key=calc_word_value)