import pytest

from divide import positive_divide

#We create a new function to test the good values
def test_positive_divide_good_values():
    assert positive_divide(4,2)==2
    assert positive_divide (2,1)==2
    assert positive_divide(-2, -1) == 2

#We create a new function to test the exceptions 
def test_positive_divide_exceptions():
    try:
        positive_divide(2, 0)
    except ZeroDivisionError:
        pytest.fail("Unexpected ZeroDivisionError!")
    with pytest.raises(TypeError):
        positive_divide(1, 's')
        positive_divide([], 2)
    with pytest.raises(ValueError):
        positive_divide(1, -2)
        positive_divide(-1, 2)

