def value(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1


def roman_to_decimal(number):
    i = 0
    result = 0
    for i in range(len(number)):
        v1 = value(number[i])
        if i + 1 < len(number):
            v2 = value(number[i + 1])
            if v1 >= v2:
                result += v1
            else:
                result -= v1
        else:
            result += v1
        i += 1
    return result


if __name__ == "__main__":
    print(roman_to_decimal("XIV"))
    print(roman_to_decimal("MCMIV"))
