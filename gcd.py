import random

def gcd(a, b):
    """
    алгоритм евклида на нахождение НОД
    """

    assert a >= 0
    assert b >= 0
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == b:
        return a

    if a > b:
        a = a % b
        return gcd(a, b)
    elif a < b:
        b = b % a
        return gcd(a, b)


def test(gcd, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0