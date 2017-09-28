from core import is_prime
print(sum(x for x in range(3, 2000000) if is_prime(x)) + 2)
