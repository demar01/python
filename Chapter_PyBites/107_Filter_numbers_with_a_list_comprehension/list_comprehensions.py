numbers= [1,2,3,4]

#easier to create two functions first and then use them in the list comprehension

def is_even(num):
    return num % 2 == 0

def is_positive(num):
    return num > 0

def filter_positive_even_numbers(numbers):
    return [number for number in numbers if is_even(number) and is_positive(number)]