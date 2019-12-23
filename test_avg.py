import average
import classly

def test_avg():
    actual_value = average.average([2,2,2,2,2])
    expected_value = 2.0
    assert actual_value == expected_value


def test_panagram1():
    actual_value = classly.panagram("abcdefghijklmnopqrstuvwxyz")
    expected_value= True
    assert actual_value == expected_value

def test_panagram2():
    actual_value = classly.panagram("adefghijklmnopqrstuvwxyz")
    expected_value= False
    assert actual_value == expected_value


                            
