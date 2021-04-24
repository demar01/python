from list_comprehensions import filter_positive_even_numbers

def test_with_negative():
    observed = filter_positive_even_numbers([1,2,3,4,-6])
    expected = [2, 4]
    assert observed == expected

def test_filter_zero_and_negatives():
    observed = filter_positive_even_numbers([0, -1, -3, -5])
    expected = []
    assert observed == expected