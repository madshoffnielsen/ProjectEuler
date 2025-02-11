def word_value(word):
    return sum(ord(char) - ord('A') + 1 for char in word)

def is_triangle_number(n):
    # A number is a triangle number if 8n + 1 is a perfect square
    x = (8 * n + 1) ** 0.5
    return x.is_integer()

def count_triangle_words(words):
    triangle_word_count = 0
    for word in words:
        if is_triangle_number(word_value(word)):
            triangle_word_count += 1
    return triangle_word_count

if __name__ == "__main__":
    with open('Solutions/0042_words.txt', 'r') as file:
        words = file.read().replace('"', '').split(',')
    result = count_triangle_words(words)
    print(f"The number of triangle words in the file is {result}")