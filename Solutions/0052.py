def has_same_digits(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

def find_permuted_multiples():
    x = 1
    while True:
        if all(has_same_digits(x, x*i) for i in range(2, 7)):
            return x
        x += 1

if __name__ == "__main__":
    result = find_permuted_multiples()
    print(f"The smallest positive integer x such that 2x, 3x, 4x, 5x, and 6x contain the same digits is {result}")