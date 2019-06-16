def linear_search(list, n, x):
    last = list[n - 1]
    list[n - 1] = x
    i = 0

    while list[i] != x:
        i+=1

    list[n - 1] = last
    if (i < n - 1) or (list[n - 1] == x):
        return i
    else:
        return "Not Found"

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Successful:", linear_search(test_list, 10, 7))
print("x is the last item:", linear_search(test_list, 10, 10))
print("Unsuccessful:", linear_search(test_list, 10, 42))
