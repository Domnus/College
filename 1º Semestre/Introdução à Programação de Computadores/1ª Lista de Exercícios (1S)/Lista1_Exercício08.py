km = float(input('KMs percorridos: '))
dias = int(input('Dias com o carro: '))

preco = (dias * 60) + (km * 0.15)

print(f'Custo total: R${preco}')