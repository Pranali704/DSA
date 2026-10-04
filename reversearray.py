
n = int(input("Enter N: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Original array =", arr)

print("Reverse array =", end=" ")

for i in range(n - 1, -1, -1):
    print(arr[i], end=" ")