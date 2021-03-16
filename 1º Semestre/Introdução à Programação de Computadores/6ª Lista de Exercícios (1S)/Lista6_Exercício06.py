from random import randint

A = []
B = []
for i in range(10):
    A.append(randint(1, 50))

print(f'Lista A : \n {A}')

x = int(input('Digite um número -> '))

for i in A:
    B.append(i * x)

print(f'Lista B : \n {B}')

