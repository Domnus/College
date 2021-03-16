from random import randint as rd

arr = []
menor = 100
menor2 = 100

for i in range(20):
    arr.append(rd(1, 100))

print('=' * 80)
print(arr)
print('=' * 80)

for i in range(20):
    for j in range(i+1, 20):
        if arr[j] < arr[i]:
            arr[j], arr[i] = arr[i], arr[j]

print(f'As duas menores notas são: {arr[0]} e {arr[1]}')

