num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

cont = 0
n1cont = 0
n2cont = 0

while cont < num1:
    cont += 1
    if num1 % cont == 0:
        n1cont += cont 
n1cont -= num1

cont = 0

while cont < num2:
    cont += 1
    if num2 % cont == 0:
        n2cont += cont
n2cont -= num2

if n1cont == num2 and n2cont == num1:
    print('Números amigos!')
else:
    print('Números inimigos! XD')
