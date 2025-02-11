def self_power_series_last_digits(limit, digits):
    modulo = 10**digits
    total = 0
    for i in range(1, limit + 1):
        power = i
        result = 1
        for _ in range(i):
            result = (result * power) % modulo
        total = (total + result) % modulo
    return total

if __name__ == "__main__":
    limit = 1000
    digits = 10
    result = self_power_series_last_digits(limit, digits)
    print(f"The last {digits} digits of the series 1^1 + 2^2 + 3^3 + ... + {limit}^{limit} is {result:010d}")