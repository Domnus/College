print('-----Número Perfeito-----')
num = int(input('Digite um número -> '))

cont = 0
x = 0

for i in range(1, num):
    cont += 1
    if (num % i) == 0:
        x += i
    
if x == num:
    print('Número Perfeito')
else:
    print('Número Não Perfeito')


