def m_order(n):
    i = 1
    while True:
        mod = (10 ** i) % n
        if mod == 1:
            return i
        if mod == 0:
            return 0
        i += 1
        if i > 1000:
            break
    return 0
    
if __name__ == "__main__":
    print("starting...")
    for i in range(2, 1000):
        m = m_order(i)
        if m > 900:
            print(i, m)