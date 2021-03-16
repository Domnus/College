from random import randint as rd

A = []
B = []
A_B = []
B_A = []

cont = 0
while cont < 10:
    a = rd(1, 20)
    if a not in A:
        A.append(a)
        cont += 1

cont = 0
while cont < 10:
    b = rd(1, 20)
    if b not in B:
        B.append(b)
        cont += 1

for i in A:
    if i in B:
        A_B.append(i)

for i in B:
    if i not in A:
        B_A.append(i)

print(f'Vetor A: \n{A}\nVetor B:\n{B}')
print(f'A-B: \n{A_B}\nB-A: \n{B_A}')

    