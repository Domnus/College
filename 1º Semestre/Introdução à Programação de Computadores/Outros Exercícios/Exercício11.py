from random import randint as rd

cartela = [0] * 5

for i in range(5):
    cont2 = 0
    cartela[i] = [0] * 5
    for j in range(5):
        cartela[i][j] = 0
          
cont1 = 1
while cont1 < 6:
    cont2 = 0
    while cont2 < 5:
        x = rd(cont1 * 15 - 14, cont1 * 15)
        if x not in cartela:
            cartela[cont2][cont1-1] = x
            cont2 += 1
    cont1 += 1

print(' B   I   N   G   O')
for i in range(0, 5):
    for j in range(5):
        print(f'[{cartela[i][j]:2}]', end='')
    print()