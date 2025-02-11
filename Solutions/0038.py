def is_pandigital(n):
    s = str(n)
    return len(s) == 9 and set(s) == set('123456789')

def concatenated_product(n, k):
    return int(''.join(str(n * i) for i in range(1, k + 1)))

def find_largest_pandigital():
    largest_pandigital = 0
    for n in range(1, 10000):
        concatenated = ''
        k = 1
        while len(concatenated) < 9:
            concatenated += str(n * k)
            k += 1
        if len(concatenated) == 9 and is_pandigital(concatenated):
            largest_pandigital = max(largest_pandigital, int(concatenated))
    return largest_pandigital

if __name__ == "__main__":
    result = find_largest_pandigital()
    print(f"The largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2,...,n) is {result}")