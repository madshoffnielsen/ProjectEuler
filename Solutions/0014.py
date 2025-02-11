def collatz_sequence_length(n, cache):
    original_n = n
    length = 0
    while n != 1:
        if n in cache:
            length += cache[n]
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    cache[original_n] = length
    return length

def longest_collatz_sequence(limit):
    max_length = 0
    starting_number = 0
    cache = {}
    for i in range(1, limit):
        length = collatz_sequence_length(i, cache)
        if length > max_length:
            max_length = length
            starting_number = i
    return starting_number

if __name__ == "__main__":
    limit = 1000000
    result = longest_collatz_sequence(limit)
    print(f"The starting number under {limit} that produces the longest Collatz sequence is {result}")