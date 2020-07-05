n, *A = map(int, input().split())
k, *B = map(int, input().split())

s = []

for i in B:
    a, b = 0, n-1
    while a <= b:
        m = int((a+b)/2)
        if A[m] == i:
            s.append(m+1)
            break
        elif A[m] > i:
            b = m - 1
        else:
            a = m + 1
    else:
        s.append(-1)
print(*s)
