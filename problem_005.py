"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def brute_force(lim=5):
    n = 0
    while True:
        n += 20
        for i in range(1, lim + 1):
            if n % i != 0:
                break
        else:
            return n


print(brute_force(lim=20))
