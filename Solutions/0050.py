def sieve_of_eratosthenes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    return [i for i in range(limit) if sieve[i]]

def find_longest_prime_sum(limit):
    primes = sieve_of_eratosthenes(limit)
    prime_set = set(primes)
    
    # Create cumulative sums
    cumulative_sums = [0]
    for prime in primes:
        cumulative_sums.append(cumulative_sums[-1] + prime)
    
    max_length = 0
    result_prime = 0
    
    # Check all possible sequences
    for i in range(len(cumulative_sums)):
        for j in range(i + max_length + 1, len(cumulative_sums)):
            sequence_sum = cumulative_sums[j] - cumulative_sums[i]
            if sequence_sum >= limit:
                break
            if sequence_sum in prime_set:
                length = j - i
                if length > max_length:
                    max_length = length
                    result_prime = sequence_sum
    
    return result_prime

if __name__ == "__main__":
    limit = 1000000
    result = find_longest_prime_sum(limit)
    print(f"The prime below {limit} that can be written as the sum of the most consecutive primes is {result}")