from random import randint as rd

A = []
B = []
soma = 0

for i in range(15):
    A.append(rd(1, 50))

for i in range(15):
    soma += A[i]
    B.append(soma)

print(f'Vetor 1: \n{A}')
print(f'Vetor 2: \n{B}')