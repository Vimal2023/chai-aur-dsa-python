from array import array

arr = array('i', [1, 2, 3, 4, 5])

# Copy & transform (multiply by 2)
new_arr = array(arr.typecode, [x * 2 for x in arr])

print(new_arr)
