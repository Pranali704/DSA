n = int(input("Enter n:"))

arr = []

for i in range(n):
    arr.append(int(input("Enter array elememt:")))

search = int(input("Enter element to search:"))

found = False

for i in range(n):
    if arr[i] == search:
        print("Element found at position ",i+1)
        found = True

if found == False:
        print("Element not found")

    


