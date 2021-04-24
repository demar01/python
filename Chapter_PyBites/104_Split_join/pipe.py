
message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def pipe(message=message):
    splitted=message.split("\n")
    joined="|".join(splitted)
    return(joined)
    #even better with map
    #return '|'.join(map(splitted, message.split('\n')))