from random import randint as rd

arr = []
arr2 = []
cont = 0

for i in range(20):
    arr.append(rd(1, 50))

print(arr)

num = int(input("Please enter ->"))

while cont <20:
    if num in arr2:
        continue
    else:
        arr2.append(rd(1, 50))
        cont += 1
        

print(f'Nova lista: \n{arr2}')