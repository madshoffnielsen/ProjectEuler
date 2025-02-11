def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    return n + int(str(n)[::-1])

def is_lychrel(n, max_iterations=50):
    for _ in range(max_iterations):
        n = reverse_and_add(n)
        if is_palindrome(n):
            return False
    return True

def count_lychrel_numbers(limit):
    count = 0
    for n in range(1, limit):
        if is_lychrel(n):
            count += 1
    return count

if __name__ == "__main__":
    limit = 10000
    result = count_lychrel_numbers(limit)
    print(f"The number of Lychrel numbers below {limit} is {result}")