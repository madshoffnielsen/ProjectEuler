def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def sum_of_primes_below(limit):
    primes = sieve_of_eratosthenes(limit)
    return sum(primes)

if __name__ == "__main__":
    limit = 2000000
    result = sum_of_primes_below(limit)
    print(f"The sum of all the primes below {limit} is {result}")