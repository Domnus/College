dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

if mes > 12 or mes < 1:
    print('Data inválida!')
elif dia < 1 or dia > 31:
    print('Data inválida!!')
elif (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    if mes == 2 and dia > 29:
        print('Data inválida!')
    else: 
        print('Data válida!')
elif mes == 2 and dia > 28:
    print('Data inválida!!')    
else:
    print('Data válida!')



