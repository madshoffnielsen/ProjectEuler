def find_recurring_cycle_length(d):
    remainders = {}
    value = 1
    position = 0

    while value != 0 and value not in remainders:
        remainders[value] = position
        value *= 10
        value %= d
        position += 1

    if value == 0:
        return 0
    else:
        return position - remainders[value]

def find_longest_recurring_cycle(limit):
    max_length = 0
    number = 0

    for i in range(2, limit):
        cycle_length = find_recurring_cycle_length(i)
        if cycle_length > max_length:
            max_length = cycle_length
            number = i

    return number

if __name__ == "__main__":
    limit = 1000
    result = find_longest_recurring_cycle(limit)
    print(f"The value of d < {limit} for which 1/d contains the longest recurring cycle is {result}")