# Bite 305. Split once, delimit many

## Description 

Write a function that accepts a string and splits the text on the specified separators, but only on the first occurrence of the delimiter.

For example:

split_once('abc: def: ijk, lmno: pqr - stu, wxy', separators=',-:')
['abc', ' def: ijk', ' lmno: pqr ', ' stu, wxy']

The separators parameter defaults to None if not supplied, in this case you should split on whitespace.


