import inspect

from recursion import countdown_for, countdown_recursive

expected = '''10
9
8
7
6
5
4
3
2
1
time is up
'''

def countdown_for_range():
    countdown_for()
    out, _ = capfd.readouterr()
    assert out == expected

