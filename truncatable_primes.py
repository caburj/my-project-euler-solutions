import numpy as np

PRIMES = np.loadtxt("100000.txt", dtype=int).flatten()

def truncate_left(num, primes):
    num_str = str(num)
    for _ in range(len(num_str)-1):
        num_str = num_str[1:]
        if not int(num_str) in primes:
            return 0
    return 1

def truncate_right(num, primes):
    num_str = str(num)
    for _ in range(len(num_str)-1):
        num_str = num_str[:-1]
        if not int(num_str) in primes:
            return 0
    return 1

def main(max_prime=1000000):
    primes = PRIMES[4:]
    primes = primes[primes< max_prime]
    count = 0
    trunc_primes = []
    for p in primes:
        if truncate_left(p, PRIMES) and truncate_right(p, PRIMES):
            count+=1
            trunc_primes.append(p)
    print(trunc_primes)
    print(count, sum(trunc_primes))

main()
