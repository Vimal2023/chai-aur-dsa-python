from array import array

arr = array('i', [3, 6, 9, 12, 15, 18])

# Delete by index
arr.pop(3)

# Delete last element
arr.pop()

# Delete by value
arr.remove(9)

print(arr)
