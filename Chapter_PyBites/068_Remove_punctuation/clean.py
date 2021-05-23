def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    table = str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    return input_string.translate(table)


# txt = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = txt.maketrans(x, y, z)
# print(txt.translate(mytable))

# remeber the pairing maketrans and translate in https://www.w3schools.com/python/ref_string_maketrans.asp


