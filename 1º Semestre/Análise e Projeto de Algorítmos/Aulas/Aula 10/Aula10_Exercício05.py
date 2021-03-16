a = []
par = []
impar = []

print('Digite 20 valores: ')
for i in range(1, 21):
    a.append(int(input('-> ')))

for i in range(0, 19):
    if a[i] % 2 == 0:
        par.append(a[i])
    else:
        impar.append(a[i])

print(f'Os valores pares são: \n{par} \nOs valores ímpares são: \n{impar}')
