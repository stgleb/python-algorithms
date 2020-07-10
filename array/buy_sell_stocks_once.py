import sys


def buy_sell_stocks_once(arr):
    min_price = sys.maxsize
    profit = 0

    for price in arr:
        if price < min_price:
            min_price = price

        profit = max(profit, price - min_price)

    return profit


if __name__ == "__main__":
    print(buy_sell_stocks_once([70, 45, 32, 47, 70, 65, 1, 40]))
