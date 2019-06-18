def binary_search(list, x):
    p = 0
    r = len(list) - 1
    while p <= r:
        q = (p + r) // 2
        if list[q] == x:
            return q
        elif list[q] > x:
            r = q - 1
        else:
            p = q + 1
    return "Not Found"


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Successful:", binary_search(test_list, 7))
print("Unsuccessful:", binary_search(test_list, 13))
