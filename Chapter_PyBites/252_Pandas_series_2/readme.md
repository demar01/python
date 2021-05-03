# Bite 252. Let's play with Pandas Series

## Description

In Bite 251 we looked at creating some simple pandas Series. In this Bite we continue where we left off and look at retrieving values and indexes of different types from Series.

You might be wondering how is this of any use to me. To remind you again Series could be considered the foundation Data Type of pandas. Dataframes are just a number of 1 dimension Series stuck together to form a 2 dimensional spreadsheet like object.

Accessing Series Elements
Now that you know how to create a Series you want to get specific elements from Series to potentially work on them in some manner. When accessing elements you have multiple options. You can access specific index locations, slices, .locand .iloc functions, research which way you think is best. How you solve this next set of challenges in not the issue, returning the expected values is the requirement to get you used to accessing specific Series indexes / values:

Return the value at the given index location
Return the slice of the Series given by the start and end slice positions
Return the slice of the Series given by the start and end positions inclusive
Return the first n elements in a Series
Return the last n elements in a Series
Return all indexes
Return all values
Return all even indexes or all odd indexes
In the next pandas Bite we will look at more advanced Series operations.