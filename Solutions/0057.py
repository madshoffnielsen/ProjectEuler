from fractions import Fraction

def count_expansions_with_more_digits(limit):
    count = 0
    fraction = Fraction(3, 2)  # First expansion
    for _ in range(1, limit):
        fraction = 1 + 1 / (1 + fraction)
        if len(str(fraction.numerator)) > len(str(fraction.denominator)):
            count += 1
    return count

if __name__ == "__main__":
    limit = 1000
    result = count_expansions_with_more_digits(limit)
    print(f"The number of fractions in the first {limit} expansions where the numerator has more digits than the denominator is {result}")