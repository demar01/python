import pytest
import re
from enumerate_data import enumerate_name_countries

expected_lines = ['1. Julian     Australia',
                  '2. Bob        Spain',
                  '3. PyBites    Global',
                  '4. Dante      Argentina',
                  '5. Martin     USA',
                  '6. Rodolfo    Mexico']

@pytest.mark.parametrize("line", expected_lines)
def test_enumerate_names_countries(capfd, line):
    enumerate_names_countries()
    output = capfd.readouterr()[0]
    #assert line in output, f'{line} not in output'
    for regex in expected_lines:
        assert re.search(regex, output)

