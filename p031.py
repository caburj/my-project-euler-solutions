import decorators


@decorators.profile
@decorators.cache
def partition(n, storage=None):
    try:
        x = storage[n]
        print 'storage called, n =', n
        return x
    except KeyError:
        answer = set()
        answer.add((n,))
        for x in range(1, n):
            for y in partition(n - x):
                answer.add(tuple(sorted((x,) + y)))
        storage[n] = answer
        return answer


@decorators.profile
def partition_nocache(n):
    answer = set()
    answer.add((n,))
    for x in range(1, n):
        for y in partition_nocache(n - x):
            answer.add(tuple(sorted((x,) + y)))
    return answer



coins = [1, 2, 5, 10, 20, 50, 100, 200]


def partition_coins(n, storage=None):
    try:
        return storage[n]
    except KeyError:
        answer = set()
        answer.add((n,))
        for i in range(len(coins)-1):
            x = coins[i]
            for y in partition(n - x):
                answer.add(tuple(sorted((x,) + y)))
        storage[n] = answer
        return answer


def parts(n):
    if n == 1:
        return [1]
    if n == 2:
        return parts(1) + parts(1)
    if n == 5:
        return parts(2) + parts(2) + parts(1)
    if n == 10:
        return parts(5) * 2
    if n == 20:
        return parts(10) * 2
    if n == 50:
        return parts(20) * 2 + parts(10)
    if n == 100:
        return parts(50) * 2
    if n == 200:
        return parts(100) * 2

print len(partition(100))

