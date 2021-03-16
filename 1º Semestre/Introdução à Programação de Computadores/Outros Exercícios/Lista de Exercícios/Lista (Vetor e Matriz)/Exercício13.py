from random import randint as rd

a1 = [0] * 10
a2 = [0] * 10
a1_2 = [0] * 10

for i in range(10):
    a1[i] = rd(1, 50)
    a2[i] = rd(1, 50)

for i in range(10):
    if i % 2 == 0:
        a1_2[i] = a1[i]
    else:
        a1_2[i] = a2[i]

print(a1)
print(a2)
print(a1_2)
