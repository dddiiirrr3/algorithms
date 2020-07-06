def numbers(n):
    """
    на вход принимает целое число n.

    возвращает список максимальной длины,
    состоящий из различных целых чисел, сумма которых дает n
    """
    assert isinstance(n, int)
    assert n >= 1

    if n <= 2:
        return [n]
    else:
        a = int((-1 + (1 + 8 * n) ** 0.5) / 2)
        s = [i for i in range(1, a + 1)]
        k = sum(s)
        if k == n:
            return s
        elif k < n:
            s = s[:-1]
            return s + [n - sum(s)]
