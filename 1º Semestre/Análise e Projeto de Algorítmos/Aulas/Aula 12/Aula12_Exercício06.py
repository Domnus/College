from random import randint
A = [0] * 4
T = [0] * 6


for i in range(4):
    A[i] = [0] * 6
    for j in range(6):
        A[i][j] = randint(0, 9)

for i in range(6):
    T[i] = [0] * 4

print('Matriz A: ')
for i in A:
    print(i)
print()

for i in range(4):
    for j in range(6):
        T[j][i] = A[i][j]

print('Matriz T:')     
for i in T:
    print(i)


