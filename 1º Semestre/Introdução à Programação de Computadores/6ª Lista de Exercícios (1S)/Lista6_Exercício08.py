from random import randint

A = []
B = []
C = []

for i in range(20):
    A.append(randint(1, 50))

for i in A:
    if i % 2 == 0:
        B.append(i)
    else:
        C.append(i)

print(f' Vetor A : {A} \n Vetor B : {B} \n Vetor C : {C}')

