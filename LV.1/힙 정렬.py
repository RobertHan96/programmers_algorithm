
case1 = [4, 1, 3, 16, 9, 10, 14, 8, 7]


def heapifiy(list, index, n):
    left = index * 2
    right = (index * 2) + 1
    start_index = index
    if left <= n and list[start_index] > list[left]:
        start_index = left
    if right <= n and list[start_index] > list[right]:
        start_index = right
    if start_index != index:
        list[index], list[start_index] = list[start_index], list[index]
        return heapifiy(list, start_index, n)


def heapSort(list):
    return 1


result = heapifiy(case1, 1, len(case1)-1)
print(result)
