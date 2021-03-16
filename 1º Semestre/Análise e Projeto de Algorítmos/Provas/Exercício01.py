arr = [0] * 20
idosos = []
soma = 0

print('Digite 20 idades:')
for i in range(20):
    x = int(input('-> '))
    arr[i] = x
    if x > 65:
        idosos.append(x)

for i in range(len(idosos)):
    for j in range(i+1, len(idosos)):
        if idosos[j] < idosos[i]:
            idosos[j], idosos[i] = idosos[i], idosos[j]
    
for i in range(len(idosos)):
    soma += idosos[i]

media = soma / len(idosos)

print(arr)
print(f'O idoso mais novo tem {idosos[0]} anos!')
print(f'A média das idades será {media}') 