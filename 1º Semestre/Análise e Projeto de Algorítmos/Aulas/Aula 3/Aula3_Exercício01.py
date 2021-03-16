sal = float(input('Salário mensal: R$'))
ven = float(input('Vendas: '))

com = (sal * 0.04) * ven
nsal = sal + com

print(f'Salário fina: R${nsal}. Comissão: R${com}.')