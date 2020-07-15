def next_number(s):
    l = list(s)
    i = 0
    output = []

    while i < len(l):
        count = 1
        start = i + 1
        while start < len(l) and l[start] == l[i]:
            start += 1
            count += 1
        output.append(str(count) + l[i])
        i = start
    return "".join(output)


def look_and_say_numbers(n):
    result = ["1"]
    i = 1

    while i < n:
        result.append(next_number(result[-1]))
        i += 1

    return result


if __name__ == "__main__":
    print(look_and_say_numbers(20))
