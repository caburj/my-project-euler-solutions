def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def is_coprime(a, b):
    return gcd(a, b) == 1

def pythagorean_triples(m, n):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return tuple(sorted([a,b,c]))

def multiply(t, c):
    return tuple(c*x for x in t)

def get_primitive_triples(m_max, n_max, max_p=1000):
    for m in range(1, m_max):
        for n in range(1, n_max):
            if m > n:
                if is_coprime(m, n) and not (m % 2 == 1 and n % 2 == 1):
                    t = pythagorean_triples(m, n)
                    if sum(t) < max_p:
                        yield t

triples = list(get_primitive_triples(100, 100))
more_triples = []

for t in triples:
    for k in range(2, 100):
        new = multiply(t, k)
        if sum(new) < 1000:
            more_triples.append(new)

all_triples = triples + more_triples

d = {}
for t in all_triples:
    try:
        d[sum(t)].append(t)
    except:
        d[sum(t)] = [t, ]

for key in d:
    print(key, len(d[key]))






