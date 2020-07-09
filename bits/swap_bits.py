def swap_bits(n, i, j):
    if n >> i & 1 != n >> j & 1:
        n = n ^ 1 << j
        n = n ^ 1 << i

    return n


if __name__ == "__main__":
    print(swap_bits(5, 2, 1))
    print(swap_bits(10, 1, 0))
