
from event import get_attendees

#solution=set(zip_longest(names, locations, confirmed, fillvalue='-'))
# solution = get_attendees()

# def assert_participant_length():
#     assert len(solution) == 30

# def assert_participant_present():
#     assert list(solution)[7][0] == 'Kim'

def test_get_attendees(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    assert len(output) == 8
    assert "('Kim', '-', '-')" in output
    assert "('Andre', '-', '-')" in output