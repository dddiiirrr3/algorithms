import time
from functools import lru_cache

import matplotlib.pyplot as plt


def memo(f):
    """
    decorator for fib1 for using cache
    """
    cache = {}

    def inner(k):
        if k not in cache:
            cache[k] = f(k)
        return cache[k]
    return inner


# @memo                    # for cache
# @lru_cache(maxsize=None)     # for cache
def fib1(k):
    """
    recursion algorithm for fibonacci numbers
    """
    assert k >= 0
    if k <= 1:
        return k
    else:
        return fib1(k-1) + fib1(k-2)


def fib2(k):
    assert k >= 0
    a = [0, 1]
    for i in range(2, k+1):
        a.append((a[i-1] + a[i-2]))
    return a[k]


def fib3(k):
    assert k >= 0
    a, b = 0, 1
    for i in range(k-1):
        a, b = b, a + b
    return b


def fib4(n, m):
    """
    функция находит остаток от деления n-ого числа Фибоначчи на число m
    """
    fibPrev = 0
    fib = 1
    cached = [fibPrev, fib]

    for curr in range(1, n):
        fibold = fib
        fib = (fib + fibPrev) % m
        fibPrev = fibold

        if fibPrev == 0 and fib == 1:
            cached.pop()
            break
        else:
            cached.append(fib)
    return cached[n % len(cached)]


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
