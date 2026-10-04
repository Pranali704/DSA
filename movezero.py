n = int(input("Enter N: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

new_arr = []

for i in range(n):
    if arr[i] != 0:
        new_arr.append(arr[i])

for i in range(n):
    if arr[i] == 0:
        new_arr.append(arr[i])

print("Array =", new_arr)

