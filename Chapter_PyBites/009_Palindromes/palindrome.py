
"""
Bite 9. Palindromes
"""
import string


"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    word = "".join(letter for letter in word if letter in string.ascii_letters)
    return word.lower() == word.lower()[::-1]
