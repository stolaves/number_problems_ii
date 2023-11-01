import pytest
import math
import random
import number_problems_2 as prog

@pytest.mark.parametrize(('n', 'res'), [(1, 1), (2, 2), (4, 6), (5, 5), (29, 31), (32, 32),(44, 66), (104, 106),  (499, 721), (235, 235), (109, 111), (112, 112), (3999, 4221), (3724, 3726)])
def test_total_roman( n, res):
    assert prog.total_roman(n) == res

@pytest.mark.parametrize(('n'), [(0),(0.00000001),("32.a"),("6f"), (4000)])
def test_total_roman_exceptions( n):
    with pytest.raises(ValueError):
        prog.total_roman(n)
