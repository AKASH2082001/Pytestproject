import Calculator

import pytest

@pytest.mark.parametrize("a,b,c",[(3,2,5),(5,1,6),(8,2,10)])
def test_Add(a,b,c):
    result= Calculator.Add(a,b)
    assert result == c
@pytest.mark.parametrize("a,b,c",[(8,3,5),(5,4,1),(8,6,2)])
def test_Sub(a,b,c):
    result= Calculator.Sub(a,b)
    assert result == c
@pytest.mark.parametrize("a,b,c",[(3,5,10),(5,7,35),(8,8,49)])
def test_Mul(a,b,c):
    result= Calculator.Mul(a,b)
    assert result == c
@pytest.mark.parametrize("a,b,c",[(4,2,2),(30,10,3),(25,5,5)])
def test_Div(a,b,c):
    result= Calculator.Div(a,b)
    assert result == c