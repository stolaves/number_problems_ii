import pytest
import math
import random
import number_problems as prog

@pytest.mark.parametrize(('n', 'res'), [(1, "I"), (2, "II"), (4, "IV"), (5, "V"), (29, "XXIX"), (32, "XXXII"),(44, "XLIV"), (104, "CIV"),  (499, "CDXCIX"), (502, "DII"), (235, "CCXXXV"), (109, "CIX"), (112, "CXII"), (3999, "MMMCMXCIX"), (3724, "MMMDCCXXIV")])
def test_roman_numeral( n, res):
    assert prog.roman_numeral(n) == res

@pytest.mark.parametrize(('n'), [(0),(-5),(0.00000001),("6f"), (4000)])
def test_roman_numeral_exceptions( n):
    with pytest.raises(ValueError):
        prog.roman_numeral(n)