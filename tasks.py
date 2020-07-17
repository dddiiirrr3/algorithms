def numbers(n):
    """
    программа выводит n чисел через пробел вида:
    1 2 2 3 3 3 4 4 4 4
    """
    s = []
    for i in range(n):
        s += [str(i+1) for k in range(i+1)]
    print(' '.join(s[:n]))


def numbers_1(n):
    print(*[int( 1/2 + (2 * i) ** 0.5) for i in range(1, n+1)])


def numbers_2(n):
    a = []
    i = 0
    while len(a) < n:
        a += [i] * i
        i += 1
    print(*a[:n])