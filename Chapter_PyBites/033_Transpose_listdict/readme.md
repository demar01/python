# Bite 33. Transpose a data structure

## Description

Sometimes you need to restructure a nested data structure. For example you can convert a dict in a list of (key, value) tuples via dict.items().

In this Bite a real world scenario where we wanted to plot some data from a Counter dict.

For plots you typically need 2 lists: X + Y axis or labels + values. So we needed an easy way to transpose data structures.

Complete the transpose function to do just that. It has to work for both dicts and lists of (named)tuples. Examples given in the docstring. See also the TESTS tab. Have fun!
