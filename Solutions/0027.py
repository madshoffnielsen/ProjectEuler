def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def number_of_consecutive_primes(a, b):
    n = 0
    while is_prime(n * n + a * n + b):
        n += 1
    return n

def find_coefficients_with_max_primes(limit_a, limit_b):
    max_primes = 0
    product = 0
    for a in range(-limit_a + 1, limit_a):
        for b in range(-limit_b, limit_b + 1):
            primes_count = number_of_consecutive_primes(a, b)
            if primes_count > max_primes:
                max_primes = primes_count
                product = a * b
    return product

if __name__ == "__main__":
    limit_a = 1000
    limit_b = 1000
    result = find_coefficients_with_max_primes(limit_a, limit_b)
    print(f"The product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n is {result}")