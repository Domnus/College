# Faça um programa que determine o mostre os cinco primeiros múltiplos de 3, considerando
# números maiores que 0.

x = True
i = 1
cont = 0

while x:
    if i % 3 == 0:
        print(i, end=" ")
        cont += 1
        i += 1
    else:
        i += 1
    if cont == 5:
        x = False
    

    