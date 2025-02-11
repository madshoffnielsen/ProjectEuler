def count_ways_to_make_change(target, coins):
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

if __name__ == "__main__":
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    result = count_ways_to_make_change(target, coins)
    print(f"The number of different ways to make £2 using any number of coins is {result}")