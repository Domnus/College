from random import randint

print('=' * 40)
while True:
    while True:
        m, n = input('Digite a dimensão da matriz A [0x0]: ').split('x')
        m = int(m)
        n = int(n)
        break

    while True:
        p, q = input('Digite a dimensão da matriz B [0x0]: ').split('x')
        p = int(p)
        q = int(q)
        break

    if m == p and n == q:
        break
    else:
        print('As matrizes devem ter as mesma dimensões para a soma!')
print('=' * 40)

A = [0] * m
for i in range(m):
    A[i] = [0] * n
    for j in range(n):
        A[i][j] = randint(1, 9)

B = [0] * p
for i in range(p):
    B[i] = [0] * q
    for j in range(q):
        B[i][j] = randint(0, 9)

print('Matriz A:')
print('=' * 40)
for i in range(m):
    for j in range(n):
        print(f'[{A[i][j]}]', end= '')
    print()
print('=' * 9)

print('Matriz B:')
print('=' * 9)
for i in range(p):
    for j in range(q):
        print(f'[{B[i][j]}]', end= '')
    print()
print('=' * 14)

Python = [0] * m
for i in range(m):
    Python[i] = [0] * n
    for j in range(n):
        Python[i][j] = A[i][j] + B[i][j]

print('Matriz Python:')
for i in range(m):
    for j in range(n):
        if Python[i][j] < 10:
            print(f'[0{Python[i][j]}]', end= '')
        else:
            print(f'[{Python[i][j]}]', end= '')
    print()
print('=' * 14)



