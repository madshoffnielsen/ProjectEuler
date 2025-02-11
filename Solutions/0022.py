def name_score(name):
    return sum(ord(char) - ord('A') + 1 for char in name)

def total_name_scores(names):
    names.sort()
    total_score = 0
    for index, name in enumerate(names):
        total_score += (index + 1) * name_score(name)
    return total_score

if __name__ == "__main__":
    with open('Solutions/0022_names.txt', 'r') as file:
        names = file.read().replace('"', '').split(',')
    result = total_name_scores(names)
    print(f"The total of all the name scores in the file is {result}")