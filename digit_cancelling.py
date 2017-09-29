from numpy import isclose

def cancel_digit(n, d):
    n1, n2 = map(int, str(n))
    d1, d2 = map(int, str(d))
    N = n1 * n2
    D = d1 * d2
    true = n / d
    try:
        false = N / D
    except ZeroDivisionError:
        false = -1
    if isclose(true, false):
        return True, n/d
    
    return False, 1
    
if __name__ == "__main__":
    prod = 1
    for d in range(10, 100):
        for n in range(10, 100):
            if n >= d:
                continue
            if n % 10 == 0 and d % 10 == 0:
                continue
            equal, val = cancel_digit(n, d)
            if equal:
                prod *= val
                print(n, d, val)
    print(1/prod)
            