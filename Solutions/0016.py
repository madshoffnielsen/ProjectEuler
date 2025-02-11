def sum_of_digits_of_power(base, exponent):
    number = base ** exponent
    return sum(int(digit) for digit in str(number))

if __name__ == "__main__":
    base = 2
    exponent = 1000
    result = sum_of_digits_of_power(base, exponent)
    print(f"The sum of the digits of the number {base}^{exponent} is {result}")