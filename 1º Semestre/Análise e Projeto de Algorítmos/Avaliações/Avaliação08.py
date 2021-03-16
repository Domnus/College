a = []
i = 0
cont1 = 0
cont2 = 0

print('Digite a nota:')
while i < 20:
    x = float(input('-> '))
    if x > 10 or x < 0:
        print('Nota inválida! Digite novamente.')
        continue
    else:
        a.append(x)
        i += 1

a.sort()

menor = a[0]
maior = a[-1]

for i in a:
    if i == menor:
        cont1 += 1
    elif i == maior:
        cont2 += 1

print(f'Menor nota = {menor} e foram {cont1} alunos que a tiraram.')
print(f'Maior nota = {maior} e foram {cont2} alunos que a tiraram.')


