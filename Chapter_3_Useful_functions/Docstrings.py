#Doctstrings provide a brief overview of the object.

def say_hello(name="Maria"):
    """A simple function that says hello... Maria style"""
    print(f"Hello {name}, what's up?")
    
#say_hello.__doc__ = "A simple function that says hello... Maria style". This is the literal way to manipulate the docstring by manipulating the __doc__ property.

help(say_hello)
print(say_hello())