def power(x, y):
    result = 1
    while y:
        if y % 2 == 0:
            x = x * x
            y = y >> 1
        else:
            result = result * x
            y -= 1
    return result


if __name__ == "__main__":
    print(power(5, 2))
    print(power(3, 5))
