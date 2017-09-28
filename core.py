import os
import numpy as np
import functools as ft
import itertools as it
import decorators


def product(series):
    return ft.reduce(lambda x, y: x * y, series)


def is_even(num):
    return num % 2 == 0


def is_prime(num):
    lim = int(np.sqrt(num)) + 1
    for i in range(2, lim):
        if num % i == 0:
            return False
    return True


def flatten(ls):
    """
    Converts a given list of list into one list.
    """
    return [item for sublist in ls for item in sublist]


@decorators.cache(init_storage={0: 1, 1: 2})
def fib_cache(n, storage=None):
    if n in storage:
        return storage[n]
    f = fib_cache(n - 1) + fib_cache(n - 2)
    storage[n] = f
    return f


@decorators.cache(init_storage=[2, 3])
def is_prime(num, storage=None):
    if num in storage:
        return True
    lim = int(np.sqrt(num))
    for i in range(2, lim + 1):
        if num % i == 0:
            return False
    storage.append(i)
    return True


def get_factors(num):
    factors = []
    lim = int(np.sqrt(num))
    for n in range(2, lim + 1):
        while num % n == 0:
            num = num / n
            factors.append(num)
            factors.append(n)
    return list(factors)
