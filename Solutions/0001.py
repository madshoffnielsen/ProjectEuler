def sum_of_multiples(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

if __name__ == "__main__":
    limit = 1000
    result = sum_of_multiples(limit)
    print(f"The sum of all multiples of 3 or 5 below {limit} is {result}")