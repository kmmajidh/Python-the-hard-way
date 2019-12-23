import classly
import random

def test_biggest():

    for count in range(1,100,3):
        n=[random.random() for _ in range(count)]
        actual = classly.biggest(n)
        expected = max(n)
        assert expected == actual

        
