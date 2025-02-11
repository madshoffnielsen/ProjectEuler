import itertools

def find_lexicographic_permutation(digits, position):
    permutations = itertools.permutations(digits)
    for i, permutation in enumerate(permutations, start=1):
        if i == position:
            return ''.join(map(str, permutation))

if __name__ == "__main__":
    digits = list(range(10))
    position = 1000000
    result = find_lexicographic_permutation(digits, position)
    print(f"The {position}th lexicographic permutation of the digits 0 to 9 is {result}")