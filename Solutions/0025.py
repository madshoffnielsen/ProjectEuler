def find_index_of_first_fibonacci_with_n_digits(n):
    a, b = 1, 1
    index = 2
    while True:
        a, b = b, a + b
        index += 1
        if len(str(b)) >= n:
            return index

if __name__ == "__main__":
    n = 1000
    result = find_index_of_first_fibonacci_with_n_digits(n)
    print(f"The index of the first term in the Fibonacci sequence to contain {n} digits is {result}")