from random import randint

A = []
B = []
C = []

print('Informe os valores dos vetores A e B:')

print('Vetor A:')
for i in range(10):
    A.append(int(input('-> ')))

print('Vetor B:')
for i in range(10):
    B.append(int(input('-> ')))


for i in A:
    if i in B:
        C.append(i)

print(A)
print(B)
print(C)
