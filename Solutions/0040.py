def champernowne_digit(position):
    length = 0
    number = 1
    while length < position:
        length += len(str(number))
        number += 1
    return int(str(number - 1)[position - length + len(str(number - 1)) - 1])

def find_champernowne_constant_product():
    product = 1
    for i in range(7):
        product *= champernowne_digit(10**i)
    return product

if __name__ == "__main__":
    result = find_champernowne_constant_product()
    print(f"The product of the digits in the Champernowne's constant at positions 1, 10, 100, 1000, 10000, 100000, and 1000000 is {result}")