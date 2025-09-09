import pytest
import math
import random
import number_problems_2 as prog

@pytest.mark.parametrize(('n', 'res'), [(1, 1), (2, 2), (4, 3), (5, 2), (29, 7), (32, 8),(44, 7), (104, 5),  (499, 12), (502, 5), (235, 12), (109, 5), (112, 6), (3999, 25), (3724, 26)])
def test_chisel_strokes( n, res):
    assert prog.chisel_strokes(n) == res