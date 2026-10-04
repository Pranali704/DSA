
arr = [10,3,45,6,8,23,42,56,30]

smin = smax = arr[0]
min = max = arr[0]

for num in arr:
    # Maximum
    if num > max:
        smax = max
        max = num
    elif num > smax and num != max:
        smax = num

    # Minimum
    if num < min:
        smin = min
        min = num
    elif num < smin and num != min:
        smin = num

print("Smallest:", min)
print("Second smallest:", smin)
print("Maximum:", max)
print("Second max:", smax)




