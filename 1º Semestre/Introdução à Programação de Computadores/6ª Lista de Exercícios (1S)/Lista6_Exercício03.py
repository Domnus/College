from random import randint

L = []
l = []

for i in range(20):
    L.append(randint(1,50))
print(L)

for n in L:
    if n % 5 == 0:
        l.append(n)

print(f'Os números divisíveis por 5 são {l}')
        
