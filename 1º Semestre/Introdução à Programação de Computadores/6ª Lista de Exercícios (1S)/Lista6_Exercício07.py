from random import randint

L = []

for i in range(10):
    L.append(randint(1, 50))

print(L)

L.sort()

print(L)