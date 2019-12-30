from prime import isprime

def test_prime_even():
    assert isprime(2) == True
    for i in range(4,100,2):
        assert isprime(i) == False
                   

def test_prime_odd():
    for i in [3,5,7,11,13]:
        assert isprime(i) == True
    for i in [9,15,35,121]:
        assert isprime(i) == False

                   
                   
    

                   
