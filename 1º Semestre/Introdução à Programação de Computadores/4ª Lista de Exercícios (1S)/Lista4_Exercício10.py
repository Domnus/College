v = ''
while v != 'Z':
    n1 = int(input('1º número: '))
    n2 = int(input('2º número: '))
    soma = n1 + n2
    if n1 > n2:
        print('O primeiro número deverá ser menor que o segundo!')
        continue
    else:
        print(f'A soma entre {n1} e {n2} é igual a {soma}.')
    v = input('Pressione qualquer tecla para continuar. Pressione "z" para parar o programa. ')
    v = v.upper()