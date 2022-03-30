import Calculator

import pytest

@pytest.mark.parametrize("a,b",[(3,2),(5,1),(8,2)])
def test_Add(a,b):
    result= Calculator.Add(a,b)
    assert result == a+b
@pytest.mark.parametrize("a,b",[(3,8),(5,4),(8,6)])
def test_Sub(a,b):

    result= Calculator.Sub(a,b)
    assert result == a-b
@pytest.mark.parametrize("a,b",[(3,5),(5,7),(8,7)])
def test_Mul(a,b):
    result= Calculator.Mul(a,b)
    assert result == a*b
@pytest.mark.parametrize("a,b",[(3,4),(5,9),(8,3)])
def test_Div(a,b):
    result= Calculator.Div(a,b)
    assert result == a/b