def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product(digits):
    max_palindrome = 0
    lower_limit = 10**(digits - 1)
    upper_limit = 10**digits
    for i in range(upper_limit - 1, lower_limit - 1, -1):
        for j in range(i, lower_limit - 1, -1):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

if __name__ == "__main__":
    digits = 3
    result = largest_palindrome_product(digits)
    print(f"The largest palindrome made from the product of two {digits}-digit numbers is {result}")