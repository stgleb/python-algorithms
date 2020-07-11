def buy_sell_stocks_twice(price):
    profit = [0] * len(price)
    n = len(price)
    max_price = price[n - 1]

    for i in range(n - 2, 0, -1):
        if price[i] > max_price:
            max_price = price[i]
        profit[i] = max(profit[i + 1], max_price - price[i])

    min_price = price[0]

    for i in range(1, n):
        if price[i] < min_price:
            min_price = price[i]

        profit[i] = max(profit[i - 1], price[i - 1] - min_price + profit[i])

    return profit[n - 1]


def buy_sell_stocks_twice2(price):
    first_profit = [0] * len(price)
    second_profit = [0] * len(price)

    # calculate data for first transaction
    min_price = price[0]
    for i in range(1, len(price)):
        if price[i] < min_price:
            min_price = price[i]
        first_profit[i] = max(first_profit[i - 1], price[i] - min_price)

    max_price = price[len(price) - 1]
    for i in range(len(price) - 2, 1, -1):
        if price[i] > max_price:
            max_price = price[i]
        second_profit[i] = max(second_profit[i + 1], max_price - price[i])

    max_profit = 0
    for i in range(len(price)):
        max_profit = max(max_profit, first_profit[i] + second_profit[i])

    return max_profit


if __name__ == "__main__":
    print(buy_sell_stocks_twice([2, 30, 15, 10, 8, 25, 80]))
    print(buy_sell_stocks_twice2([2, 30, 15, 10, 8, 25, 80]))
