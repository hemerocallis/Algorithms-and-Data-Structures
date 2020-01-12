def quickSort(array):
    if len(array) < 2:
        return array
    else:
        baseItem = array[0]
        less = [i for i in array[1:] if i <= baseItem]
        greater = [i for i in array[1:] if i > baseItem]
        return quickSort(less) + [baseItem] + quickSort(greater)

array = [5, 3, 42, 13, 7, 23, 13]
print(quickSort(array))
