from random import randint

L = []
Q = []
for i in range(10):
    L.append(randint(1, 50))

for i in range(len(L)):
    Q.append(L[i]**2)

print(L)
print(Q)

