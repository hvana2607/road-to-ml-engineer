import pytest
@pytest.mark.parametrize("a,b,expected",[(2,3,5),(0,0,0),(-1,1,0)])
def test_add_many(a,b,expected):
    assert add(a,b)==expected

def add(a,b):
    return a+b

def test_add():
    assert add(2,3)==5

def test_add_negitive():
    assert add(-1,-1) == -2

def test_add_with_fixture(sample_number):
    a,b = sample_number
    print("values from fixture:", a, b)
    assert add(a,b)==30

def test_add_with_fixture2(sample_number):
    a, b = sample_number
    assert add(a, b) == 30