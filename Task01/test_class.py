import pytest
from triangle_class import Triangle, IncorrectTriangleSides

def test_equilateral():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 9

def test_isosceles():
    t = Triangle(3, 3, 2)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 8

def test_nonequilateral():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12

def test_invalid_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 5)

def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 3, 4)

def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-3, 3, 3)
