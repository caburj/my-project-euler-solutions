import itertools
import myfuncs
import p012

def proper_divisors(factors):
    divisors = []
    for i in range(1, len(factors)):
        for ls in itertools.combinations(factors, i):
            divisors.append(myfuncs.product(ls))
    divisors.append(1)
    return list(set(divisors))


def is_amicable(num):
    factors = p012.all_factors(num)
    divisors = proper_divisors(factors)
    sum_divisors = sum(divisors)
    if num == sum_divisors:
        return False
    factors = p012.all_factors(sum_divisors)
    divisors = proper_divisors(factors)
    return num == sum(divisors)


print sum(x for x in range(2, 10001) if is_amicable(x))
