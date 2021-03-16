import random

pila = float(input('Valor da entrada: R$'))

x = random.randint(1,100)
y = random.randint(1,100)
z = random.randint(1,100)

print(x)
print(y)
print(z)

if x == y and y == z:
    print(f'Parabéns! Você conseguiu 3 números iguais e ganhou R${pila*100}!')
elif x == y or y == z or x == z:
    print(f'Parabéns! Você conseguiu 2 números iguais e ganhou R${pila*5}!')
else:
    print('Mais sorte da próxima vez!')
