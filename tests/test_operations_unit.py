import operations
import pytest

def test_add():
    assert operations.add(1,2) == 3
    assert operations.add(1.5,2.5) == 4.0

def test_sub():
    assert operations.sub(5,3) == 2
    assert operations.sub(3.2,1.2) == 2.0

def test_mul():
    assert operations.mul(4,5) == 20
    assert operations.mul(2.5,2) == 5.0

def test_div():
    assert operations.div(10,2) == 5
    assert pytest.approx(operations.div(1,3), rel=1e-6) == 1/3

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        operations.div(1,0)
