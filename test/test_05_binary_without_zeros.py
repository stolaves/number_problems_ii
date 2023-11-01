import pytest
import math
import random
import number_problems_2 as prog

@pytest.mark.parametrize(('n', 'res'), [(1, 1), (2, 1), (3, 11), (6, 11), (14, 111), (31, 11111),(32, 1), (78, 1111),  (466, 11111), (4003, 11111111), (58287, 11111111111), (912126, 111111111111111), (3678478730, 1111111111111), (620177531616132, 111111111111111111111), (91459483565536760843, 11111111111111111111111111111111111)])
def test_binary_without_zeros( n, res):
    assert prog.binary_without_zeros(n) == res

@pytest.mark.parametrize(('n'), [(0),(-5),(0.00000001),("6f"), ("325235s")])
def test_binary_without_zeros_exceptions( n):
    with pytest.raises(ValueError):
        prog.binary_without_zeros(n)
