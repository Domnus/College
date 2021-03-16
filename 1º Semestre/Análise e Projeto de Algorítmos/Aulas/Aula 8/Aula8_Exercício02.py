print('-----Fatorial-----')
num = int(input('Digite um número -> '))
f = 1

if (num < 0):
    print('Não existe fatorial')
else:
    for i in range(num, 1, -1):
        f *= i

print(f'Fatorial: {f}')