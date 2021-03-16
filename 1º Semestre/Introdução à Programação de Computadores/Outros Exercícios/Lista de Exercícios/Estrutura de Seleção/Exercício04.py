idade = int(input('Idade: '))
tempoServiço = int(input('Tempo de Serviço: '))

if idade >= 60 and tempoServiço >= 25:
    print('Pode aposentar!')
elif tempoServiço >= 30 or idade >= 65:
    print('Pode aposentar!')
else:
    print('Não pode aposentar!')