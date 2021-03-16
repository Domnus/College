while True:
    k = int(input('Função Resto \n-> '))
    m = int(input('-> '))

    if m > 0:
        if k > 0:
            result = k % m
        elif k < 0:
            result2 = (k * -1) % m
            result = m - result2
        print(result)
    else:
        print('Número inválido!')


