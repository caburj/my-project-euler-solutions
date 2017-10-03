def palindrome(num_str):
    reverse = "".join(reversed(num_str))
    return num_str == reverse

def main(max_val):
    double_pals = []
    for i in range(1, int(max_val)):
        d = str(i)
        b = bin(i)[2:]
        if all(map(palindrome, [d, b])):
            double_pals.append(i)
    print(sum(double_pals))

main(1e6)


