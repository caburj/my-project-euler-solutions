from math import factorial as f

def get_digits(n):
    return map(int, str(n))
    
def factorials(max=1000):
    i = 3
    fact = f(i)
    while fact < max:
        yield fact
        i += 1
        fact = f(i)

if __name__ == "__main__":
    numbers = []
    for num in range(3, 2540160):
        digits = get_digits(num)
        total = sum(map(f, digits))
        if total == num:
            numbers.append(total)
    print(numbers)
    print(sum(numbers))