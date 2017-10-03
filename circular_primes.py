import numpy as np
from core import is_prime

primes = np.loadtxt("100000.txt", dtype=int).flatten()
primes = primes[primes < 1000000]

def rotations(prime, primes=primes):
    num_str = str(prime)
    vals = []
    print(prime)
    for _ in range(len(num_str)-1):
        num_str = num_str[1:] + num_str[0:1]
        num = int(num_str)
        if not num in primes:
            return 0
    return 1
        
if __name__ == "__main__":
    print(sum(map(rotations, primes)))
    

