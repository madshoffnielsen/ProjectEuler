def combinations(n, r):
    if r > n - r:
        r = n - r
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (n - i)
        denominator *= (i + 1)
    return numerator // denominator

def count_large_combinations(limit):
    count = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if combinations(n, r) > limit:
                count += 1
    return count

if __name__ == "__main__":
    limit = 1000000
    result = count_large_combinations(limit)
    print(f"The number of values of C(n,r) for 1 ≤ n ≤ 100 that are greater than {limit} is {result}")