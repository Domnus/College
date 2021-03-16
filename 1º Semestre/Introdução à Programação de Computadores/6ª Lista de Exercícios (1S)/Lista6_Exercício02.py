from random import randint

L = []

for i in range(20):
    L.append(randint(1,50))
print(L)

qpar = 0 
spar = 0
for i in L:
    if i % 2 == 0:
        spar += i
        qpar += 1

media = spar / qpar

print(f'A média dos números pares é igual a {media:.2f}')

