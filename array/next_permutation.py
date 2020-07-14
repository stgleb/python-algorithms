def next_permutation(permutation):
    swap_index = -1

    for i in range(len(permutation) - 1, 0, -1):
        if permutation[i - 1] < permutation[i]:
            swap_index = i - 1
            break

    if swap_index == -1:
        return permutation

    for i in range(len(permutation) - 1, swap_index, -1):
        if permutation[swap_index] < permutation[i]:
            permutation[swap_index], permutation[i] = permutation[i], permutation[swap_index]
            break

    return permutation[:swap_index + 1] + permutation[swap_index + 1:][::-1]


if __name__ == "__main__":
    perm = [1, 2, 3, 4]

    for i in range(24):
        print(perm)
        perm = next_permutation(perm)