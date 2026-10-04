arr = [10,7,30,31]

even = 0
odd = 0

for i in range(len(arr)):
    if(arr[i] % 2 == 0):
        even = even + 1

    else:
        odd = odd + 1

print("even cnt:",even)
print("odd cnt:",odd)


