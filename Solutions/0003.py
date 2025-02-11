def largest_prime_factor(n):
    # Start with the smallest prime factor
    factor = 2
    # Divide out all factors of 2
    while n % factor == 0:
        n //= factor
    # Check odd factors from 3 upwards
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 2
    # If n is still greater than 2, then it is prime
    if n > 2:
        return n
    return factor

if __name__ == "__main__":
    number = 600851475143
    result = largest_prime_factor(number)
    print(f"The largest prime factor of {number} is {result}")