import numpy as np
from core import is_prime

primes = np.loadtxt("100000.txt", dtype=int).flatten()
primes = primes[primes < 1000000]

consecutive_sums = {}

for i in range(primes.size):
    for j in range(i+1, primes.size):
        s = sum(primes[i:j])
        n = j - i
        if s > 1000000:
            break
        consecutive_sums[n] = s

for key in reversed(sorted(consecutive_sums)):
    num = consecutive_sums[key]
    if is_prime(num):
        print(num)