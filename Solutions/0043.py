from itertools import permutations

def has_substring_divisibility_property(pandigital):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        if int(pandigital[i:i+3]) % primes[i-1] != 0:
            return False
    return True

def find_sum_of_pandigital_numbers():
    pandigital_sum = 0
    for perm in permutations('0123456789'):
        pandigital = ''.join(perm)
        if has_substring_divisibility_property(pandigital):
            pandigital_sum += int(pandigital)
    return pandigital_sum

if __name__ == "__main__":
    result = find_sum_of_pandigital_numbers()
    print(f"The sum of all 0 to 9 pandigital numbers with the substring divisibility property is {result}")