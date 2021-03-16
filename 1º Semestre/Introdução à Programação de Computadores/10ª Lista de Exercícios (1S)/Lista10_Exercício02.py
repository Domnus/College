while True:
    h1 = int(input('Homem 1 -> '))
    h2 = int(input('Homem 2 -> '))
    m1 = int(input('Mulher 1 -> '))
    m2 = int(input('Mulher 2 -> '))
    if h1 == h2 or m1 == m2:
        print('As idades dos homens ou das mulheres não podem ser iguais!')
    else:
        if h1 > h2:
            hvelho = h1
            hnovo = h2
        else:
            hvelho = h2
            hnovo = h1
        if m1 > m2:
            mvelha = m1
            mnova = m2
        else:
            mvelha = m2
            mnova = m1
        break
    
print(f'Homem + velho e mulher + nova = {hvelho + mnova}')
print(f'Homem + novo e mulher + velha = {hnovo * mvelha}')