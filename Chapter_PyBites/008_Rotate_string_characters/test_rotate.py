from rotate import rotate


def test_small_rotate():
    assert rotate('hello', 2) == 'llohe'
    assert rotate('hello', -2) == 'lohel'



def test_rotation_of_n_bigger_than_string():
    string = 'hello!'
    expected_solution1 = 'hello!'
    expected_solution2 = 'llohe'  # ;)
    assert rotate(string, 2) in (expected_solution1,
                                   expected_solution2)