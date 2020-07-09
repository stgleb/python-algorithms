def reverse_bits(n):
    ret, power = 0, 31
    while n:
        ret += (n & 1) << power
        n = n >> 1
        power -= 1
    return ret


if __name__ == "__main__":
    print(reverse_bits(5))
    print(reverse_bits(6))
