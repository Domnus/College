from random import randint as rd

arr = []
proibido = []
obrigatorio = []
facultativo = []

for i in range(50):
    x = rd(0, 100)
    arr.append(x)
    if x < 16:
        proibido.append(x)
    elif x > 65:
        facultativo.append(x)
    elif x > 18 and x < 65:
        obrigatorio.append(x)
    
print(arr)
print(proibido)
print(obrigatorio)
print(facultativo)




