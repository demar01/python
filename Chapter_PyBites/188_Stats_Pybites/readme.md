# Bite 188. Get statistics from PyBites test code

## Description 

Did you know Python has a statistics module?

For this Bite we did a line count on our test code for 186 Bites, running this command: wc -l */test_*.py|sort -n -k2|grep -v total > testfiles_number_loc.txt. Output:

$ head -5 testfiles_number_loc.txt
      13 01/test_numbers.py
      17 02/test_regex.py
      23 03/test_wordvalue.py
      15 04/test_tags.py
      21 05/test_names.py
       ...

Complete the stats dict wih all the relevant metrics producing the following output:

Basic statistics:
- count     :     186
- min       :       6
- max       :     337
- mean      :   43.74

Population variance:
- pstdev    :   43.04
- pvariance : 1852.39

Estimated variance for sample:
- count     :   93.00
- stdev     :   30.24
- variance  :  914.36

We already did the formatting for you, so just focus on completing stats using a combination of Python builtins and the statistics module.

We retrieved this example from Python 3 Module of the Week (link provided upon resolving this Bite ...)

Make sure you check out statistics docs while coding this Bite. Other than that, keep calm and code some stats in Python!

