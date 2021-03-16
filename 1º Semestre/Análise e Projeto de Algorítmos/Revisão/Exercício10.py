arr = [0] * 5

for i in range(5):
    arr[i] = [0] * 5

num = 1
inicio = 0
fim = 5

while (num <=25):
    for j in range(inicio, fim):
        arr[inicio][j] = num
        num += 1

    for i in range(inicio+1, fim):
        arr[i][fim-1] = num
        num += 1

    for j in range(fim-2, inicio-1, -1):
        arr[fim-1][j] = num
        num += 1
    
    for i in range(fim-2, inicio, -1):
        arr[i][inicio] = num
        num += 1

    inicio += 1
    fim -= 1

print('=' * 15)
for i in range(5):
    for j in range(5):
        print(f'[{arr[i][j]:2}]', end='')
    print()
print('=' * 15)

    
