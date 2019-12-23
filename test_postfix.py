import classly
import pytest
def test_postfix1():
    actual = classly.postfix("325*+")
    expected = 3+2*5
    assert actual == expected
    
def test_postfix2():
    actual = classly.postfix("32578+-*/")
    expected =3/(2*(5-(7+8)))
    assert actual == expected

def test_postfix3():
    with pytest.raises(ZeroDivisionError):
        classly.postfix("30/")

        
