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

def is_truncatable_prime(n):
    if n < 10:
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i + 1])):
            return False
    return True

def find_truncatable_primes(limit):
    truncatable_primes = []
    num = 11  # The smallest two-digit prime number
    while len(truncatable_primes) < limit:
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
        num += 2  # Only check odd numbers
    return truncatable_primes

if __name__ == "__main__":
    limit = 11  # There are exactly 11 truncatable primes
    truncatable_primes = find_truncatable_primes(limit)
    result = sum(truncatable_primes)
    print(f"The sum of the only {limit} truncatable primes is {result}")