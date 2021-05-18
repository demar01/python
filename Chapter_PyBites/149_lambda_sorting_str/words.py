def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    return sorted(words, key=lambda x: (x[0].isdigit(), x.lower())) #what x[0] it does is cheching the first character of the word (so 2 in 2019 and C in Christmas). Then isdigit returns true or false 

# words = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019".split()
# sorted(i.lower() for i in words) #this is not enough cuz the year still goes to the beggining
# sorted(words, key=lambda x: x.lower()) # but this is how it will translate into lambda
# sorted((i[0].isdigit(), i.lower()) for i in words) # once that this is past, 2019 is pushed to the end. But this is not exaclty what we want, cuz this is a list of tuples [('False','a')...]
# [(i[0].isdigit(),i.lower()) for i in words] #this is how it would be as a list comprehension
# sorted(words, key=lambda x: (x[0].isdigit(), x.lower())) #somewhat doing it as a lambda output the correct thing, aka not [('False','a')...] but actually ['a'...]


