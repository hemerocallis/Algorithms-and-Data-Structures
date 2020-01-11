def findSmallestItem(array):
    smallestItem = array[0]
    smallestItemIndex = 0
    for i in range(1, len(array)):
        if array[i] < smallestItem:
            smallestItem = array[i]
            smallestItemIndex = i
    return smallestItemIndex

def selectionSort(array):
    newArray = []
    for i in range(len(array)):
        smallestItemIndex = findSmallestItem(array)
        newArray.append(array.pop(smallestItemIndex))
    return newArray

array = [10, 6, 4, 3, 8, 1, 9, 2, 7, 5]
print(selectionSort(array))
