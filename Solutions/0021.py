def sum_of_divisors(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def find_amicable_numbers(limit):
    amicable_sum = 0
    for a in range(2, limit):
        b = sum_of_divisors(a)
        if b != a and b < limit and sum_of_divisors(b) == a:
            amicable_sum += a
    return amicable_sum

if __name__ == "__main__":
    limit = 10000
    result = find_amicable_numbers(limit)
    print(f"The sum of all amicable numbers under {limit} is {result}")