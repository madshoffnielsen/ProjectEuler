def sieve_of_eratosthenes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    return sieve

def get_prime_family_size(prime_str, pattern, sieve):
    family_size = 0
    first_prime = None
    for digit in '0123456789':
        num = int(prime_str.replace('*', digit))
        if num >= len(sieve) or len(str(num)) != len(prime_str):
            continue
        if sieve[num]:
            family_size += 1
            if first_prime is None:
                first_prime = num
    return family_size, first_prime

def find_prime_with_pattern():
    limit = 1000000
    sieve = sieve_of_eratosthenes(limit)
    
    for length in range(2, 7):
        for num in range(10**(length-1), 10**length):
            if not sieve[num]:
                continue
            
            num_str = str(num)
            # Try different patterns of replacements
            for digit in set(num_str):
                pattern = num_str.replace(digit, '*')
                if pattern.count('*') == 0:
                    continue
                    
                family_size, first_prime = get_prime_family_size(pattern, digit, sieve)
                if family_size == 8:
                    return first_prime
    
    return None

if __name__ == "__main__":
    result = find_prime_with_pattern()
    print(f"The smallest prime which, by replacing part of the number with the same digit, is part of an eight prime value family is {result}")