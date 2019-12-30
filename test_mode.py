from stat_mode import mode

def test_mode0():
    assert mode([]) == 0

def test_mode1():
    assert mode([1]) == 1

def test_moden():
    assert mode([1,2,3,4,5,67,84,4,4,4,5,7,8,6,45,4,3,4,4,]) == 4

def test_mode=():
    assert mode([1,2,1,2,1,2,1,2,1,2]) == 0
