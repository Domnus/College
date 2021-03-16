from random import randint as rd

arr = [0] * 10
mo = 0
num = 0

for i in range(10):
    arr[i] = rd(1, 7)

for i in range(10):
    cont = 0
    for j in range(10):
        if arr[i] == arr[j]:
            cont += 1
    if cont > mo:
        num = arr[i]
        mo = cont

print(arr)
print(f'O número {num} apareceu {mo} vezes')