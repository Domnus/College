precoProduto = float(input('Preço do Protudo: '))
estado = (input('Estado de destino: ')).upper()

if estado == 'MG':
    precoProduto *= 1.07
    print(f'O preço do produto será R${precoProduto}')
elif estado == 'SP':
    precoProduto *= 1.12
    print(f'O preço do produto será R${precoProduto}')
elif estado == 'RJ':
    precoProduto *= 1.15
    print(f'O preço do produto será R${precoProduto}')
elif estado == 'MS':
    precoProduto *= 1.08
    print(f'O preço do produto será R${precoProduto}')
else:
    print('Estado Inválido!')
