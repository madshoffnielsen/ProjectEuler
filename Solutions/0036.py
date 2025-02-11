def is_palindrome(s):
    return s == s[::-1]

def is_double_base_palindrome(n):
    decimal_str = str(n)
    binary_str = bin(n)[2:]
    return is_palindrome(decimal_str) and is_palindrome(binary_str)

def sum_of_double_base_palindromes(limit):
    total_sum = 0
    for i in range(limit):
        if is_double_base_palindrome(i):
            total_sum += i
    return total_sum

if __name__ == "__main__":
    limit = 1000000
    result = sum_of_double_base_palindromes(limit)
    print(f"The sum of all numbers, less than {limit}, which are palindromic in base 10 and base 2 is {result}")