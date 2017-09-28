"""special pythagorean triplet"""


def pythagorean_triplet(total=1000):
    for a in range(1, 1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if a + b + c == total and a ** 2 + b ** 2 == c ** 2:
                    print(a, b, c)
                    return a, b, c
    return []


from core import product

print(product(pythagorean_triplet(1000)))
