import pytest

from rounding_even import round_even

@pytest.mark.parametrize("input_float, int", [
    (0.40000000000000002220446049250313080847263336181640625, 0),
    (0.5, 0),
    (0.6, 1),
    (1.4, 1),
    (1.5, 2),
    (1.6, 2),
    (2.5, 2), # nearest even int
])
def test_round_even(input_float, int):
    assert round_even(input_float) == int