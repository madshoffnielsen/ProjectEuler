def sieve_of_eratosthenes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    return [i for i in range(limit) if sieve[i]]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_pair(p1, p2, prime_cache={}):
    pair = (p1, p2)
    if pair in prime_cache:
        return prime_cache[pair]
    n1 = int(str(p1) + str(p2))
    n2 = int(str(p2) + str(p1))
    result = is_prime(n1) and is_prime(n2)
    prime_cache[pair] = result
    return result

def find_prime_set():
    primes = sieve_of_eratosthenes(10000)
    prime_cache = {}
    
    for i, p1 in enumerate(primes):
        if p1 > 10000: break
        for j, p2 in enumerate(primes[i+1:], i+1):
            if not check_pair(p1, p2, prime_cache):
                continue
            for k, p3 in enumerate(primes[j+1:], j+1):
                if not (check_pair(p1, p3, prime_cache) and check_pair(p2, p3, prime_cache)):
                    continue
                for l, p4 in enumerate(primes[k+1:], k+1):
                    if not (check_pair(p1, p4, prime_cache) and check_pair(p2, p4, prime_cache) 
                           and check_pair(p3, p4, prime_cache)):
                        continue
                    for m, p5 in enumerate(primes[l+1:], l+1):
                        if (check_pair(p1, p5, prime_cache) and check_pair(p2, p5, prime_cache) 
                            and check_pair(p3, p5, prime_cache) and check_pair(p4, p5, prime_cache)):
                            return p1 + p2 + p3 + p4 + p5

if __name__ == "__main__":
    result = find_prime_set()
    print(f"The sum of the five primes is {result}")