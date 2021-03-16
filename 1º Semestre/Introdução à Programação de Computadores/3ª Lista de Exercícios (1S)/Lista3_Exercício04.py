sal = float(input('Valor do salário: '))
emp = float(input('Valor da prestação do empréstimo: '))

if emp > (sal*0.2):
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')
    