from random import randint

L = []

for i in range(10):
    L.append(randint(1, 50))

print('Digite 1 para ver a lista na ordem normal \nDigite 2 para ver a lista na ordem reversa')

while True:
    x = int(input('-> '))
    if x == 1:
        print(L)
        break
    elif x == 2:
        L.reverse()
        print(L)
        break
    else:
        print('Número inválido!')
        continue