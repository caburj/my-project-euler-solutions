from core import is_even

counts = {1: 1}


def collatz(n, orig_n, container):
    container.append(n)
    try:
        counts[orig_n] = len(container) + counts[n] - 1
    except KeyError:
        if is_even(n):
            return collatz(n / 2, orig_n, container)
        return collatz(3 * n + 1, orig_n, container)


for i in range(3, 1000000, 2):
    cont = []
    collatz(i, i, cont)
print(counts.keys()[counts.values().index(max(counts.values()))])
