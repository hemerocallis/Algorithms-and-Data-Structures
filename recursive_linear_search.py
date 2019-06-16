def recursive_linear_search(list, n, i, x):
    if i > n - 1:
        return "Not Found"
    else:
        if list[i] == x:
            return i
        else:
            return recursive_linear_search(list, n, i + 1, x)

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Successful:", recursive_linear_search(test_list, 10, 0, 7))
print("x is the last item:", recursive_linear_search(test_list, 10, 0, 10))
print("Unsuccessful:", recursive_linear_search(test_list, 10, 0, 42))
