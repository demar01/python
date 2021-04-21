from palindrome import is_palindrome


def test_is_palidrome():
    assert is_palindrome('Aibohphobia')
    assert is_palindrome('Avid diva')
    assert is_palindrome('Avid diva. ')
    assert is_palindrome('A Toyota’s a Toyota.')
    assert is_palindrome('A man, a plan, a canal: Panama')
    assert is_palindrome("No 'x' in 'Nixon'")
    assert is_palindrome('malayalam')

    assert not is_palindrome('PyBites')
    assert not is_palindrome('malayalan')
    assert not is_palindrome('toyota')
    assert not is_palindrome('palindrome')


test_is_palidrome()