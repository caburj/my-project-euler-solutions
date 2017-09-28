def diagonals(n=5):
    n2 = n**2
    vals = []
    for i in range(4):
        vals.append(n2-i*(n-1))
    return vals

def sum_diagonals(n=5):
    total = 1
    for i in range(2, n, 2):
        for x in diagonals(i+1):
            total += x
    return total

if __name__ == "__main__":
    print(sum_diagonals(n=1001))