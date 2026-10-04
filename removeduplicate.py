n = int(input("Enter N: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

new_arr = []

for i in range(n):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])

print("Array after removing duplicates =", new_arr)