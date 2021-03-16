from random import randint

L = []

for i in range(10):
    L.append(randint(1, 51))
print(L)

x = int(input('Digite um número que deseja encontrar na lista: \n-> '))

for i in L:
    if x not in L:
        print(f'{x} não perterce à lista.')
        break
    else:
        print(f'{x} pertence à lista' )
        break