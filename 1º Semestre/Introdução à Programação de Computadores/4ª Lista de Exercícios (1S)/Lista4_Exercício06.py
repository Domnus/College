x = int(input('Quantos números deseja somar? '))
par = 0
impar = 0
cont = 0
while cont < x:
    num = int(input('Digite um número: '))
    if (num % 2) == 0:
        par += num
    else:
        impar += num
    cont += 1

print(f'Soma dos números pares: {par}') 
print(f'Soma dos números ímpares: {impar}')
