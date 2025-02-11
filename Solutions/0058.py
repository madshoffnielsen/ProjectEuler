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

def find_spiral_side_length():
    side_length = 1
    number = 1
    prime_count = 0
    total_diagonals = 1
    
    while True:
        side_length += 2
        for _ in range(4):
            number += side_length - 1
            if is_prime(number):
                prime_count += 1
        total_diagonals += 4
        if prime_count / total_diagonals < 0.1:
            return side_length

if __name__ == "__main__":
    result = find_spiral_side_length()
    print(f"The side length of the square spiral for which the ratio of primes along both diagonals first falls below 10% is {result}")