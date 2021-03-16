from random import randint

A = []
print('Informe 10 elementos:')
for i in range(10):
    A.append(int(input('-> ')))

for i in range(10):
    for j in range(i + 1, 10):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

print(A)