def is_palindrome(s):
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("hello it is me"))
    print(is_palindrome("sbbs"))
