import math

def sum_of_digit_factorials(n):
    return sum(math.factorial(int(digit)) for digit in str(n))

def find_curious_numbers(limit):
    curious_numbers = []
    for i in range(10, limit):
        if i == sum_of_digit_factorials(i):
            curious_numbers.append(i)
    return curious_numbers

if __name__ == "__main__":
    # 7 * 9! is 2540160, so we use this as an upper limit
    limit = 7 * math.factorial(9)
    curious_numbers = find_curious_numbers(limit)
    result = sum(curious_numbers)
    print(f"The sum of all numbers which are equal to the sum of the factorial of their digits is {result}")