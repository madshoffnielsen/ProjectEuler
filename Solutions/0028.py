def sum_of_spiral_diagonals(size):
    total_sum = 1  # Starting with the center value 1
    current_number = 1
    for layer in range(1, (size // 2) + 1):
        step = layer * 2
        for _ in range(4):
            current_number += step
            total_sum += current_number
    return total_sum

if __name__ == "__main__":
    size = 1001
    result = sum_of_spiral_diagonals(size)
    print(f"The sum of the numbers on the diagonals in a {size}x{size} spiral is {result}")