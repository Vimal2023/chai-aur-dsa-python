from array import array

arr = array('i', [1, 2, 3, 4, 5, 6])

# Using index
for i in range(len(arr)):
    print(arr[i], end=" ")

print()

# Enhanced for loop
for x in arr:
    print(x, end=", ")
