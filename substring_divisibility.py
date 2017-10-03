from itertools import permutations

def pandigital_with_zero(n=10):
    for p in permutations(range(n)):
        if p[0] != 0:
            yield p

def check(n):
    nums = []
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        nums.append(int("".join(map(str, n[i:i+3]))))
    return all(n % d == 0 for n, d in zip(nums, divisors))

def to_int(pandigital):
    return int("".join(map(str, pandigital)))

total = 0
for pandigital in pandigital_with_zero():
    print(pandigital)
    if check(pandigital):
        total += to_int(pandigital)

print(total)
