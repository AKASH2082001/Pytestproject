import Calculator

def test_Add():
    x=10
    y=2
    result= Calculator.Add(x,y)
    assert result == x+y

def test_Sub():
    x=10
    y=2
    result= Calculator.Sub(x,y)
    assert result == x-y

def test_Mul():
    x=10
    y=2
    result= Calculator.Mul(x,y)
    assert result == x*y

def test_Div():
    x=10
    y=2
    result= Calculator.Div(x,y)
    assert result == x/y