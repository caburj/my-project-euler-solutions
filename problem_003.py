"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


import math
import core
import decorators


def get_max_prime_factor(factors):
    for factor in reversed(factors):
        if core.is_prime(factor):
            return factor
    return None


def test_is_prime():
    print('is %s prime? %s' % (10, core.is_prime(10)))
    print('is %s prime? %s' % (11, core.is_prime(11)))
    print('is %s prime? %s' % (100, core.is_prime(100)))


def test_get_factors():
    print(core.get_factors(891))
    print(core.get_factors(100))
    print(core.get_factors(34137))


if __name__ == '__main__':
    test_is_prime()
    test_get_factors()
    print(get_max_prime_factor(core.get_factors(600851475143)))
