def reverse_words_and_string(l):
    reverse_range(l, 0, len(l) - 1)

    start, end = 0, 0

    while start < len(l) - 1:
        end = start
        while end < len(l) and l[end] != ' ':
            end += 1
        reverse_range(l, start, end - 1)
        start = end

        while start < len(l) and l[start] == ' ':
            start += 1


def reverse_range(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


if __name__ == "__main__":
    text = list("hello it is me")
    reverse_words_and_string(text)
    print("".join(text))
