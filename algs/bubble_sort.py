my_arr = [234, 1, 3, 5, 2, 12, 34, 523, 232, 12, 2234]

n = len(my_arr)
for i in range(n-1):
    swapped = False
    for j in range(n - i - 1):
        if my_arr[j] > my_arr[j + 1]:
            my_arr[j], my_arr[j + 1] = my_arr[j + 1], my_arr[j]
            swapped = True
    if not swapped:
        break

print("Sorted Array", my_arr)