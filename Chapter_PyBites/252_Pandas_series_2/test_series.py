import inspect
import string

import pytest
import numpy as np
import pandas as pd

import series as se


@pytest.fixture()
def float_series():
    """Returns a pandas Series containing floats"""
    return pd.Series([float(n) / 1000 for n in range(0, 1001)])

@pytest.mark.parametrize("arg, expected", [
    (0, 0.000), (500, 0.500), (1000, 1.000)
])
def test_return_at_index(float_series, arg, expected):
    assert se.return_at_index(float_series, arg) == expected


def test_return_at_index_raise_exception(float_series):
    with pytest.raises(KeyError):
        float_series[1111]


def test_get_slice(float_series):
    slce = se.get_slice(float_series, 20, 25)
    assert isinstance(slce, pd.core.series.Series)
    assert len(slce) == 5
    assert slce[24] == 0.024

def test_get_slice_inclusive(float_series):
    slce = se.get_slice_inclusive(float_series, 20, 25)
    assert isinstance(slce, pd.core.series.Series)
    assert len(slce) == 6
    assert slce[25] == 0.025
