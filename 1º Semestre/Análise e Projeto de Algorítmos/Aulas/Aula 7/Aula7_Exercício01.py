c = True

while c:
    nota = float(input('Digite a nota: '))
    if nota < 0 or nota > 10:
        print('Nota inválida')
    else:
        print('Nota válida')
    c = nota < 0 or nota > 10
