from array import array

arr = array('i', [1, 2, 3, 4, 5])

# Insert at index
arr.insert(1, 50)

# Append at end
arr.append(100)

# Update element
arr[2] = 200

print(arr)
