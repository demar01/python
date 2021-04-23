from kwargs import get_profile

import pytest

def kwargs_default():
    assert get_profile()=='julian is a programmer'

def kwargs_other_dict():
    assert get_profile(profession='barista', name='bob') =='bob is a barista'


def kwargs_one_pos_arg():
    with pytest.raises(TypeError): #to me this order of defyning the test is kind of inverted
        get_profile('julian')

def test_wrong_single_kw():
    with pytest.raises(TypeError):
        get_profile(test=True)