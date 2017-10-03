from core import is_prime
from itertools import permutations

def possible_prime_pandigitals(n):
    l = permutations(range(1,n+1), n)
    for p in l:
        if p[-1] in (1, 3, 7, 9):
            yield int("".join(map(str, p)))


def max_pandigital_prime(n_digits=5):
    pandigitals = possible_prime_pandigitals(n_digits)
    for p in reversed(list(pandigitals)):
        if is_prime(p):
            return p


print(max_pandigital_prime(7))

