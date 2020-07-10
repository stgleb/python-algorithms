def dutch_flag_sort(arr):
    l, m, r = 0, 0, len(arr) - 1

    while m < r:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
        elif arr[m] == 1:
            m += 1
        elif arr[m] == 2:
            arr[r], arr[m] = arr[m], arr[r]
            r -= 1
    return arr


if __name__ == "__main__":
    print(dutch_flag_sort([2, 2, 1, 0, 1, 1, 2, 0, 1, 2, 2]))
