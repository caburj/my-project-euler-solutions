from itertools import permutations, product

def check_pandigital(product, remaining):
    """
    product : int
    remaining : str
    """
    product = str(product)
    if len(product) == len(remaining):
        return "".join(sorted(product)) == "".join(sorted(remaining))
    return False
    
def n_digit_permutations(n):
    return permutations(range(1, 10), n)
    
def n_digit_permutations_minus_digits(n, digits):
    """
    digits : tuple -> to be removed from range(1, 10)
    n : int -> number of digits in the combination
    """
    remaining = list(range(1, 10))
    for d in digits:
        remaining.remove(d)
    return permutations(remaining, n)
    
def main():
    one_digits = list(n_digit_permutations(2))
    four_digits = {}
    for one_digit in one_digits:
        four_digits[one_digit] = [list(n_digit_permutations_minus_digits(3, one_digit))]
    
    for key in four_digits:
        single = key
        fours = list(four_digits[key][0])
        remainings = []
        for four in fours:
            remaining = list(range(1, 10))
            for d in single+four:
                remaining.remove(d)
            remainings.append(remaining)
        four_digits[key].append(remainings)
    
    # print(four_digits)
    total = []
    for key in four_digits:
        single = int("".join(map(str, key)))
        fours = [int("".join(map(str, four))) for four in four_digits[key][0]]
        remainings = ["".join(map(str, remaining)) for remaining in four_digits[key][1]]
        products = [single*four for four in fours]
        # total += list(prod for prod, rem in zip(products, remainings) 
                          # if check_pandigital(prod, rem))
        products = []
        for four, rem in zip(fours, remainings):
            prod = single * four
            if check_pandigital(prod, rem):
                print(single, four, prod)
                products.append(prod)
            
    print(sum(total))
    # for d in one_digits+four_digits:
        # remaining.remove(d)
    # remaining = "".join(remaining)
    # one_digits = [int("".join(digits)) for digits in one_digits]
    # four_digits = [int("".join(digits)) for digits in four_digits]
    # all_one_by_four = product(one_digits, four_digits)
    # products = [a*b for a, b in all_one_by_four]
    # total = sum(product for product in products if check_pandigital(product, remaining))
    # print(total)
    
if __name__ == "__main__":
    main()