def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def find_max_digit_sum(limit):
    max_sum = 0
    for a in range(1, limit):
        for b in range(1, limit):
            current_sum = digit_sum(a ** b)
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

if __name__ == "__main__":
    limit = 100
    result = find_max_digit_sum(limit)
    print(f"The maximum digital sum of a^b for 1 ≤ a, b < {limit} is {result}")