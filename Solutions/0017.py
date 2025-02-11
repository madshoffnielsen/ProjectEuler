def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    def words(n):
        if n < 10:
            return ones[n]
        elif 10 < n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + (ones[n % 10] if n % 10 != 0 else "")
        elif n < 1000:
            return ones[n // 100] + "hundred" + ("and" + words(n % 100) if n % 100 != 0 else "")
        elif n == 1000:
            return "onethousand"
    
    return words(n)

def total_number_letter_count(limit):
    total_count = 0
    for i in range(1, limit + 1):
        total_count += len(number_to_words(i).replace(" ", "").replace("-", ""))
    return total_count

if __name__ == "__main__":
    limit = 1000
    result = total_number_letter_count(limit)
    print(f"The total number of letters used to write all the numbers from 1 to {limit} is {result}")