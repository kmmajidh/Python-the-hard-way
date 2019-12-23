import classly

def test_fizzbizz():
    a = classly.fizzbizz(20)
    e = [1,2,"fizz",4,"bizz","fizz",7,8,"fizz","bizz",11,"fizz",13,14, "fizzbizz", 16, 17, "fizz", 19, "bizz"]
    assert a == e

def test_fizzbizz1():
    a = classly.fizzbizz(0)
    e = 0
    assert a==e

