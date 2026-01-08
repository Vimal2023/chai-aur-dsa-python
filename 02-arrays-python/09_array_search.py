from array import array

arr = array('i', [12, 23, 45, 67, 89, 134])

try:
    index = arr.index(45)
    print("Element found at index:", index)
except ValueError:
    print("Element not found")
