def is_pentagonal(x):
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()

def is_hexagonal(x):
    n = (1 + (1 + 8 * x) ** 0.5) / 4
    return n.is_integer()

def find_next_tri_pent_hex_number(start):
    n = start
    while True:
        triangle_number = n * (n + 1) // 2
        if is_pentagonal(triangle_number) and is_hexagonal(triangle_number):
            return triangle_number
        n += 1

if __name__ == "__main__":
    start = 286  # Starting from the next number after 285
    result = find_next_tri_pent_hex_number(start)
    print(f"The next triangle number that is also pentagonal and hexagonal is {result}")