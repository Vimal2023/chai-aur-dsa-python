from array import array

arr = array('i', [])

n = int(input("Enter number of elements: "))

for _ in range(n):
    value = int(input("Enter next number: "))
    arr.append(value)

print("Final Array:")
for x in arr:
    print(x, end=" ")
