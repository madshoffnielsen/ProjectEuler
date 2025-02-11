def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def find_triangle_number_with_divisors(limit):
    triangle_number = 0
    i = 1
    while True:
        triangle_number += i
        if count_divisors(triangle_number) > limit:
            return triangle_number
        i += 1

if __name__ == "__main__":
    limit = 500
    result = find_triangle_number_with_divisors(limit)
    print(f"The first triangle number with over {limit} divisors is {result}")