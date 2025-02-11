
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def are_permutations(a, b, c):
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c))

def find_sequence():
    for i in range(1000, 10000):
        if not is_prime(i):
            continue
        for j in range(i + 1, 10000):
            if not is_prime(j):
                continue
            k = j + (j - i)  # Third term in arithmetic sequence
            if k >= 10000:
                break
            if is_prime(k) and are_permutations(i, j, k):
                if i != 1487:  # Skip known sequence
                    return str(i) + str(j) + str(k)
    return None

if __name__ == "__main__":
    result = find_sequence()
    print(f"The 12-digit number is {result}")