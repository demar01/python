  
from regex import (has_timestamp, is_integer)


def test_has_timestamp():
    assert has_timestamp('INFO 2014-07-03T23:27:51 Shutdown initiated.')
    assert has_timestamp('INFO 2014-06-01T13:28:51 Shutdown initiated.')
    assert not has_timestamp('INFO 2014-7-3T23:27:51 Shutdown initiated.')
    assert not has_timestamp('INFO 2014-07-03t23:27:1 Shutdown initiated.')


def test_is_integer():
    assert is_integer(1)
    assert is_integer(-1)
    assert not is_integer('str')
    assert not is_integer(1.1)