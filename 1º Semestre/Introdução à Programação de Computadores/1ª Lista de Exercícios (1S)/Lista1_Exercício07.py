preco = float(input('Preço do combustível: '))
desemp = float(input('Desempenho do veículo: '))
dist = float(input('Distância entre as cidades: '))

litros = dist / desemp
pcomb = litros * preco

print(f'Litros gastos: {litros}. Gasto na viagem: R${pcomb}.')