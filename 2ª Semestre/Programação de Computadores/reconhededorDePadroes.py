while True:
    estado0 = True
    estado1 = False
    estado2 = False
    estado3 = False
    y = []
    x = input("Digite o valor em binário: ")
    
    for i in range(len(x)):
        if estado0:
            if x[i] == '1':
                estado1 = True
                estado0 = False
                y.append('0')
            else:
                estado3 = False
                estado2 = False
                estado1 = False
                estado0 = True
        if estado1:
            if x[i] == '1':
                estado2 = True
                estado1 = False
                y.append('0')
            else:
                estado2 = False
                estado0 = True
        if estado2:
            if x[i] == '1':
                estado3 = True
                estado2 = False
                y.append('0')
            else:
                estado3 = False
                estado0 = True
        if estado3:
            if x[i] == '1':
                estado3 = True
                estado2 = False
                y.append('1')
            else:
                estado0 = True
    print(y)
    






