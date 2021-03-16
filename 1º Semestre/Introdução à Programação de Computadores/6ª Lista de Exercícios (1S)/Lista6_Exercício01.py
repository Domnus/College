from random import randint

L = []
for i in range(10):
    L.append(randint(1,50))

par = 0
impar = 0

for n in L:
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(L)
print(f'Há {par} números pares e {impar} números ímpares')
    