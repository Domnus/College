x = 0
par = 0
impar = 0

while x < 10:
    num = int(input('Digite um número: '))
    if (num % 2) == 0:
        par += num
    else:
        impar += num
    x += 1

print(f'Soma dos números pares: {par}')
print(f'Soma dos números ímpares: {impar}')
