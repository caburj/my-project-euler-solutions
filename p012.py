from core import product
import math
from collections import Counter


def all_factors(num):
    lim = int(math.sqrt(num))
    factors = []
    for i in range(2, lim + 1):
        while num % i == 0:
            factors.append(i)
            num = num / i
    if num != 1:
        factors.append(num)
    return factors


def counter(factors):
    return Counter(factors).values()


def number_of_divisors(counts):
    ls = [x + 1 for x in counts]
    return product(ls)


def solution(max_count=5):
    tri_num = 1
    n = 1
    while True:
        n += 1
        tri_num += n
        if number_of_divisors(counter(all_factors(tri_num))) >= max_count:
            print(tri_num)
            break


if __name__ == '__main__':
    test_num = 3
    factors = all_factors(test_num)
    counts = Counter(factors).values()
    num = number_of_divisors(counts)
    print (factors)
    print (counts)
    print (num)

    solution(500)
