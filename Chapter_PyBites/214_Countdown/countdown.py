from itertools import islice


def countdown():
    """Write a generator that counts from 100 to 1"""
    for i in reversed(range(1, 101)): 
    #for i in range(100, 0, -1):
        yield i