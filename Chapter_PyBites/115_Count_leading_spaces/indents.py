from itertools import takewhile


def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return sum(1 for _ in list(takewhile(lambda x: x == ' ', text)))