import math

def isprime(n):
    if n%2 == 0:
        return n == 2

    limit = math.ceil(math.sqrt(n))

    for i in range(2, n):
        if n%i == 0:
            return False
    return True

    
