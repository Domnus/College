fp = open('agenda.txt', 'a+')

while True:
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    fp.write(nome + " " + telefone + "\n")

    while True:
        resp = input('Quer continuar? [sn]').upper()[0]
        if resp in 'SN':
            break
        print('Entrada inválida!')
    if resp == 'N':
        break

fp.seek(0)
print(fp.read())
