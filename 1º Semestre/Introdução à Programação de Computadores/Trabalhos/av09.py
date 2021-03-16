from random import randint

A = []
B = []
C = []

for i in range(10):
    A.append(randint(1, 50))
    B.append(randint(1, 50))

B.reverse()
for i in range(10):
    C.append(A[i] + B[(i)])

print(f'Vetor A: \n {A}')
print(f'Vetor B: \n {B}')
print(f'Vetor C: \n {C}')