def reverse(l):
    buf = []
    result = []
    stack = []

    for i in range(len(l)):
        if s[i] == '(':
            stack.append(i)

        if s[i] != '(' and s[i] != ')':
            buf.append(s[i])

        if s[i] == ')':
            if len(result) == 0:
                result.append(buf[::-1])
            else:
                if i - stack[-1] - 1 == len(buf):
                    result[-1] = result[-1] + buf[::-1]
                else:
                    result[-1] = result[-1] + buf
                    result[-1] = result[-1][::-1]

                del stack[-1]
            buf = []

        if s[i] == '(':
            if len(buf) > 0:
                result.append(buf)
                buf = []

    return result


if __name__ == "__main__":
    s = "hello(skeeg(for)skeeg)"
    print(reverse(list(s)))
