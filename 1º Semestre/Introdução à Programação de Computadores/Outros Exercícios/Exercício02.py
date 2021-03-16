print('-----Soma dos dígitos de um número-----')
n = int(input('Digite um número-> '))

soma = 0
while n > 0:
    soma += n % 10
    n //= 10

print(f'A soma dos dígitos é igual a {soma}')

    

