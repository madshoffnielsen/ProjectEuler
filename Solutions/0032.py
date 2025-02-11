def is_pandigital(n, digits):
    n_str = str(n)
    return len(n_str) == digits and set(n_str) == set(str(i) for i in range(1, digits + 1))

def find_pandigital_products():
    products = set()
    for a in range(1, 100):
        for b in range(a, 10000 // a):
            product = a * b
            combined = str(a) + str(b) + str(product)
            if len(combined) == 9 and is_pandigital(combined, 9):
                products.add(product)
    return sum(products)

if __name__ == "__main__":
    result = find_pandigital_products()
    print(f"The sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital is {result}")