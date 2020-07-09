def count_ones(n):
    count = 0
    while n:
        count += 1
        n = n & (n - 1)

    return count


if __name__ == "__main__":
    print(count_ones(5))
    print(count_ones(15))
