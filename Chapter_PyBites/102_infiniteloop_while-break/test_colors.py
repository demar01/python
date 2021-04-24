from unittest.mock import patch

from colors import print_colors


@patch("builtins.input", side_effect=['blue', 'Yellow', 'white',
                                      'red', 'Orange', 'quit'])
def test_print_colors(input_mock, capfd): 
    expected = '\n'.join(['blue', 'yellow', 'Not a valid color', 'red',
                          'Not a valid color', 'bye'])

    print_colors()

    output = capfd.readouterr()[0].strip()
    assert output == expected