def insertion_sort(arr):
    if len(arr) == 0:
        return None

    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = temp
    return arr


arr = [2, 3, 9, 8, 5]

print(insertion_sort(arr))
