"""" Testing lambda comprehension module"""

from Lambda_comprehension import int_sort

def test_int_sort_empty() -> None:
    """Integer sort should behave as expected"""
    assert(int_sort(['id1', 'id2', 'id30', 'id3', 'id22', 'id100'])==['id1', 'id2', 'id3', 'id22', 'id30', 'id100'])

#python3 -m pytest Chapter3/Lambda_comprehension_test.py 
