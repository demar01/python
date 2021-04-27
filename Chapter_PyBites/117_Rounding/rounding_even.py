
def round_even(number): 
    return int(round(number, 0))

from decimal import Decimal

def round_even(number):
    """Takes a number and returns it rounded even"""
    return int(Decimal(number).to_integral_value())

# int(round(0.4, 0))
# int(round(0.40000000000000002220446049250313080847263336181640625, 0))

