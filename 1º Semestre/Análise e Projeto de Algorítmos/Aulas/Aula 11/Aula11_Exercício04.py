from random import randint

A = []
B = []
C = []

print('Informe os valores dos Vetores A e B: ')

print('Vetor A:')
for i in range(10):
    A.append(int(input('-> ')))

print('Vetor B:')
for i in range(10):
    B.append(int(input('-> ')))

for i in A:
    C.append(i)
    
for i in B:
    if i not in A:
        if i not in C:
            C.append(i)

print(A)
print(B)
print(C)