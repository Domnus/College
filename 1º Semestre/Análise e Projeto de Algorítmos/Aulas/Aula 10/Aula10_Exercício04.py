a = []
b = []
PE = 0

print('Informe 10 valores para o vetor A: ')
for i in range(1, 11):
    a.append(int(input('-> ')))

print('Informe 10 valores para o vetor B: ')
for i in range(1, 11):
    b.append(int(input('-> ')))

for i in range(0, 10):
    PE += a[i] * b[i]

print(f'O produto escalar dos vetores A e B é \n{PE}')