def add(x, y):
    while y:
        carry = x & y
        x, y = x ^ y, carry << 1

    return x


def multiply(x, y):
    result = 0
    while x:
        if x & 1:
            result = add(result, y)
        y <<= 1
        x >>= 1

    return result


if __name__ == "__main__":
    print(add(5, 2))
    print(multiply(7, 3))
    print(multiply(8, 4))
