def quick_sort(array, left, right):
    if left < right:
        position = partition(array, left, right)
        quick_sort(array, left, position - 1)
        quick_sort(array, position + 1, right)

    return array


def partition(array, left, right):
    pivot = array[right]
    low = left - 1

    for i in range(left, right):
        if array[i] <= pivot:
            low += 1
            swap(array, i, low)
    swap(array, right, low + 1)
    return low + 1


def swap(array, i, low):
    temp = array[i]
    array[i] = array[low]
    array[low] = temp
