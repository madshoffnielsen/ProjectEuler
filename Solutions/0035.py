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

def get_rotations(n):
    rotations = []
    s = str(n)
    for i in range(len(s)):
        rotation = s[i:] + s[:i]
        rotations.append(int(rotation))
    return rotations

def is_circular_prime(n):
    rotations = get_rotations(n)
    return all(is_prime(rotation) for rotation in rotations)

def count_circular_primes(limit):
    count = 0
    for i in range(2, limit):
        if is_circular_prime(i):
            count += 1
    return count

if __name__ == "__main__":
    limit = 1000000
    result = count_circular_primes(limit)
    print(f"The number of circular primes below {limit} is {result}")