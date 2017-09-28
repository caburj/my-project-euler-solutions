""" 10001st prime """


from core import is_prime

n = 3
count = 2
lim = 10001
while True:
    n += 2
    if is_prime(n):
        print n
        count += 1
        if count == lim:
            break
