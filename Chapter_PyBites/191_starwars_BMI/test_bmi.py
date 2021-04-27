from bmi import person_max_bmi, data


def test_person_max_bmi():
    assert person_max_bmi() == ('Yoda', 39.03)


def test_person_max_bmi_smaller_dataset():
    newdata = '\n'.join(data.splitlines()[:2])
    assert person_max_bmi(newdata) == ('C-3PO', 26.89)


def test_person_max_bmi_another_smaller_dataset():
    newdata = '\n'.join([character for character in data.splitlines()
                         if character.lstrip()[:4] not in ('C-3PO', 'Yoda')])
    assert person_max_bmi(newdata) == ('Owen Lars', 37.87)