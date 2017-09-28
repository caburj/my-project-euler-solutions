"""
Problem 27
"""

from core import is_prime

def quad(a, b):
    return lambda n: n**2+a*n+b

def efficient_quad_primes(max_coeff=1000):
    list_primes = list(x for x in range(2, 1000) if is_prime(x))
    coefficients = 0, 0
    current_max = 0
    for a in list(-x for x in list_primes)+list_primes:
        for b in list(-x for x in list_primes)+list_primes:
            n = 0
            print(a, b)
            quad_func = quad(a, b)
            val = quad_func(n)
            while val > 1 and is_prime(val):
                n += 1
                val = quad_func(n)
            print(n)
            if n > current_max:
                current_max = n
                coefficients = a, b
    return coefficients, current_max

if __name__ == "__main__":
    print(efficient_quad_primes(1000))