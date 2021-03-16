a = []
b = []
c = []
print('Informe 10 números inteiros para o vetor A: ')

for i in range(1, 11):
    a.append(int(input('-> ')))

print('Informe 10 números inteiros para o vetor B: ')

for i in range(1, 11):
    b.append(int(input('-> ')))

for i in range(0, 10):
    c.append(a[i] + b[i]) 

print(f'Vetor C = \n{c}')


