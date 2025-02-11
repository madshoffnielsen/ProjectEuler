import math

def sum_of_factorial_digits(n):
    factorial = math.factorial(n)
    return sum(int(digit) for digit in str(factorial))

if __name__ == "__main__":
    number = 100
    result = sum_of_factorial_digits(number)
    print(f"The sum of the digits in the number {number}! is {result}")