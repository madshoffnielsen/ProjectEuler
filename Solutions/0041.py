from itertools import permutations

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

def find_largest_pandigital_prime():
    digits = '987654321'
    for i in range(len(digits)):
        for perm in permutations(digits[i:]):
            num = int(''.join(perm))
            if is_prime(num):
                return num
    return None

if __name__ == "__main__":
    result = find_largest_pandigital_prime()
    print(f"The largest n-digit pandigital prime is {result}")