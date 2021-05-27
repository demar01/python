# Bite 241. Write tests for list_to_decimal

## Description

Note this is a Test Bite and uses Python 3.7 and MutPy 0.6.1


Our 4th test Bite. Michael made a calculator that will be able to accept a list of decimal digits and returns an integer where each int of the given list represents decimal place values from first element to last.

He wrote the function in such a way that it only accepts positive digits in range(0, 10) and anything that is not raises a ValueError if its out of range, or a TypeError if its not an int type.

Some examples:

[0, 4, 2, 8] => 428
[1, 2] => 12
[3] => 3
[6, 2, True] => raises TypeError
[-3, 12] => raises ValueError
[3.6, 4, 1] => raises TypeError
['4', 5, 3, 1] => raises TypeError
In this Bite you are tasked to write the tests for this function. Good luck and keep calm and code in Python!
