def swap_bits(n, i, j):
    if n >> i & 1 != n >> j & 1:
        n = n ^ 1 << j
        n = n ^ 1 << i
    return n


# Find closest integer number with same count of bits set to 1
def closest(n):
    i = 0
    while 1 << i < n:
        if (1 << i + 1) & n != (1 << i) & n:
            return swap_bits(n, i + 1, i)
        i += 1
    return n


if __name__ == "__main__":
    print(closest(5))
    print(closest(17))
    print(closest(10))
