def sum(array):
    if len(array) == 1:
        return array[0]
    else:
        newArray = [i for i in array[1:]]
        return array[0] + sum(newArray)

array = [0, 1, 2, 3]
print(sum(array))
