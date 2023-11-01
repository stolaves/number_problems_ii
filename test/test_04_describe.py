import pytest
import math
import random
import number_problems_2 as prog

@pytest.mark.parametrize(('n', 'res'), [(0, 10), (1, 11), (10, 1110), (11, 21), (22, 22), (60, 1610),(921,191211), (9781, 19171811),  (31201, 1311121011), (44243, 24121413), (54687, 1514161817), (650517, 161510151117), (7041627, 17101411161217), (399155165020, 13291125111615101210), (822226421763575, 184216141211171613151715)])
def test_describe( n, res):
    assert prog.describe(n) == res

@pytest.mark.parametrize(('n'), [(-6),(-5),(0.00000001),("6f"), ("Helolowe")])
def test_describe_exceptions( n):
    with pytest.raises(ValueError):
        prog.describe(n)
