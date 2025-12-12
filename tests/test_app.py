import sys
from pathlib import Path
import math
from math import pi
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, mul, sin, sub

def test_add():
    assert add(5, 6) == 11

def test_sub():
    assert sub(5, 2) == 3


def test_add2():
    assert add(5, 6) != 10

def test_mul():
    assert mul(4, 5) == 20

def test_sin_zero():
    assert sin(0) == 0

def test_sin_pi_over_two():
    assert sin(pi/2) == 1