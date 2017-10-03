def pentagons(n_max=1000):
    for n in range(1, n_max+1):
        yield n * (3*n - 1) // 2



