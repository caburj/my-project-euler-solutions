def is_pandigital(num):
    num_str = str(num)
    return "".join(sorted(num_str)) == "".join(map(str, range(1, 10)))

def main(n=9):
    string = ""
    for i in range(1, 100):
        string += str(n*i)
        if len(string) >= 9:
            break
    return (string, is_pandigital(string))

for n in range(1, 1000000):
    string, ispan = main(n)
    if ispan:
        print(string)

