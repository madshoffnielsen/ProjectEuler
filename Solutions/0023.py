def sum_of_divisors(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def is_abundant(n):
    return sum_of_divisors(n) > n

def find_abundant_numbers(limit):
    return [i for i in range(12, limit) if is_abundant(i)]

def can_be_written_as_sum_of_two_abundants(n, abundant_numbers):
    abundant_set = set(abundant_numbers)
    for a in abundant_numbers:
        if a >= n:
            break
        if (n - a) in abundant_set:
            return True
    return False

def sum_of_non_abundant_sums(limit):
    abundant_numbers = find_abundant_numbers(limit)
    total_sum = 0
    for i in range(1, limit):
        if not can_be_written_as_sum_of_two_abundants(i, abundant_numbers):
            total_sum += i
    return total_sum

if __name__ == "__main__":
    limit = 28123
    result = sum_of_non_abundant_sums(limit)
    print(f"The sum of all the positive integers which cannot be written as the sum of two abundant numbers is {result}")