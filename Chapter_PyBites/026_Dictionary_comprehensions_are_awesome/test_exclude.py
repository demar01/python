from exclude import filter_dic, exclude_bites

def test_filter_bites():
    result = filter_dic()
    assert type(result) == dict
    assert len(result) == 10
    for bite in exclude_bites:
        assert bite not in result, f'Bite {bite} should not be in result'