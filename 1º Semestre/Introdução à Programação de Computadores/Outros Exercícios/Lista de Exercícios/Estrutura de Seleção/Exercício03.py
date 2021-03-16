print('-------------------')
print('Área de um trapézio')
print('-------------------')

while True:
    bm = float(input('Base maior-> '))
    if bm < 0:
        print('Deve ser maior que 0.')
    else:
        break

while True:
    bmn = float(input('Base menor-> '))
    if bmn < 0:
        print('Deve ser maior que 0.')
    else:
        break

while True:
    alt = float(input('Altura-> '))
    if alt < 0:
        print('Deve ser maior que 0.')
    else:
        break
    

A = ((bm + bmn) * alt) / 2
print(f'A área do trapézio é {A}')
 
