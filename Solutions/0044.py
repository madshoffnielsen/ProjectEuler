def pentagonal_number(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()

def find_minimal_pentagonal_difference():
    pentagonals = set()
    n = 1
    while True:
        pn = pentagonal_number(n)
        for pj in pentagonals:
            if is_pentagonal(pn - pj) and is_pentagonal(pn + pj):
                return pn - pj
        pentagonals.add(pn)
        n += 1

if __name__ == "__main__":
    result = find_minimal_pentagonal_difference()
    print(f"The minimal difference of pentagonal numbers for which their sum and difference are pentagonal is {result}")