# Bite 75. Parse Unix cal to a weekday mapping

## Description 

Unix has a similar tool to look up a week day for a certain date: cal, for example:

$ cal 4 2018
     April 2018
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30

In this Bite we are going to ignore the existance of Python's calendar module for a minute and do a parsing Kata. Complete the get_weekdays function below that takes a multiline string output from the Unix cal command (see the TESTS tab for examples) and convert it to a mapping (dict) where the keys are day ints and the values are the 2 letter week days (Su Mo Tu ...).

This way it's easy to lookup any date and get the week day returned (again see how we use the function in the tests)

Sure you might put this off as useless because there is a module to work with dates and calendar, but the point is to be able to convert an output into a workable data structure, a goto skill for any Python endeavor ranging from log parsing (related: Bite 7. Parsing dates from logs) to required data cleaning for plotting, etc.

String manipulation (you might use regexes and slicing here), looping, populating a dict, are Pythonic skills you will use over and over again. So good luck and have fun!

