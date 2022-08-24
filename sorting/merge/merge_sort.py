def merge_sort(my_list):

    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, my_list)
    return my_list


def merge(left, right, my_list):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            my_list[k] = left[i]
            i += 1
        else:
            my_list[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1
    else:
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
