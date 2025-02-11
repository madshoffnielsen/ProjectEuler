def get_prime_factors(n):
    factors = set()
    d = 2
    while n > 1:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.add(n)
            break
    return factors

def has_n_distinct_factors(n, required_factors):
    return len(get_prime_factors(n)) == required_factors

def find_consecutive_numbers(consecutive_count, required_factors):
    n = 2
    count = 0
    while True:
        if has_n_distinct_factors(n, required_factors):
            count += 1
            if count == consecutive_count:
                return n - consecutive_count + 1
        else:
            count = 0
        n += 1

if __name__ == "__main__":
    consecutive_count = 4
    required_factors = 4
    result = find_consecutive_numbers(consecutive_count, required_factors)
    print(f"The first of {consecutive_count} consecutive integers to have exactly {required_factors} distinct prime factors is {result}")