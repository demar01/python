#Some decorators warm up

# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped

# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# @makebold
# @makeitalic
# def hello():
#     return "hello world"

#Because we need to decorate a function with arguments, we need to use *args and **kwargs in the inner wrapper function. Then it will accept an arbitrary number of positional and keyword arguments.

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice
 
# @do_twice
# def say_whee():
#     print("Whee!")

# say_whee()

# @do_twice
# def greet(name):
#     print(f"Hello {name}")

# greet("Bob")





from functools

UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="


def sandwich(func):
    """Write a decorator that prints UPPER_SLICE and
       LOWER_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """
    @functools.wraps(func)
    def wrapped_decorator(*args, **kwargs):
        print(UPPER_SLICE)
        arguments= func(*args, **kwargs)
        print(LOWER_SLICE)
        return arguments
    return wrapped_decorator

@sandwich
def add_ingredients(ingredients):
    print(' / '.join(ingredients))

ingredients = ['bacon', 'lettuce', 'tomato']
add_ingredients(ingredients)

