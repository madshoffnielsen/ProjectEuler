def sum_of_fifth_powers(limit):
    total_sum = 0
    for number in range(2, limit):
        if number == sum(int(digit) ** 5 for digit in str(number)):
            total_sum += number
    return total_sum

if __name__ == "__main__":
    # The upper limit is set to 6 * 9^5 because 9^5 * 6 is the highest number we need to check
    limit = 6 * (9 ** 5)
    result = sum_of_fifth_powers(limit)
    print(f"The sum of all the numbers that can be written as the sum of fifth powers of their digits is {result}")