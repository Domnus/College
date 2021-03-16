x = 0
y = 1
while x < 10:
    print(f'{y}º Aluno: ')
    n1 = float(input('1ª Nota: '))
    if n1 < 0 or n1 > 10:
        print('Nota inválida!')
        continue
    else:    
        n2 = float(input('2ª Nota: '))
        if n2 < 0 or n2 > 10:
            print('Nota inválida!')
            continue
        else:
            m = (n1 + n2) / 2
            print(f'A média é igual a {m}')
            x += 1
            y += 1