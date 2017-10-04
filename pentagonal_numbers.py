N = 100000
n = 10000

pen = lambda n : n * (3*n - 1) // 2
pens = list(pen(x) for x in range(1, N))

from math import sqrt
def is_pentagonal(n):
    k = (sqrt(24*n+1)+1)/6
    return k.is_integer()

for i in range(n//2-1, N-n//2):
    for j in range(-n//2, n//2):
        # print(i, j)
        pi = pens[i]
        pj = pens[i+j]
        total = pi + pj
        diff = abs(pj - pi)
        if is_pentagonal(total) and is_pentagonal(diff):
            print(pi, pj, total, diff)

print("End of iteration.")