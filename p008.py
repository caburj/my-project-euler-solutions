"""
largest product in a series
"""


from core import product

with open('data_p008') as f:
    ls = f.read().strip().split('\n')
    series = [int(x) for x in list(''.join(ls))]


def brute_force(series, length=4):
    container = []
    for i in range(len(series) - length):
        container.append(product(series[i:i + length]))
    return max(container)


print(brute_force(series, length=13))
