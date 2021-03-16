income = float(input('Salário-> '))
prestacao = float(input('Prestação do Empréstimo-> '))

x = income * 0.2
if prestacao > x:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')

