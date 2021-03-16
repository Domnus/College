from random import randint as rd

arr = []

for i in range(20):
    arr.append(rd(1, 30))

print(arr)

for i in range(10):
    arr[i], arr[19-i] = arr[19-i], arr[i]
    
print(arr)