def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_goldbach(n):
    i = 1
    while 2 * i * i <= n:
        if is_prime(n - 2 * i * i):
            return True
        i += 1
    return False

def find_goldbach_failure():
    n = 9
    while True:
        if not is_prime(n) and n % 2 == 1:
            if not check_goldbach(n):
                return n
        n += 2

if __name__ == "__main__":
    result = find_goldbach_failure()
    print(f"The smallest odd composite that cannot be written as the sum of a prime and twice a square is {result}")