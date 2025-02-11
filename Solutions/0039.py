def find_perimeter_with_max_solutions(limit):
    max_solutions = 0
    best_perimeter = 0

    for p in range(2, limit + 1, 2):
        solutions = 0
        for a in range(2, p // 3):
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                solutions += 1
        if solutions > max_solutions:
            max_solutions = solutions
            best_perimeter = p

    return best_perimeter

if __name__ == "__main__":
    limit = 1000
    result = find_perimeter_with_max_solutions(limit)
    print(f"The value of p ≤ {limit} for which the number of solutions is maximized is {result}")