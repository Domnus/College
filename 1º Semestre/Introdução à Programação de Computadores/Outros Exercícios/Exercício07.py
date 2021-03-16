from random import randint

x = []
y = 0

while y < 20:
    i = randint(1, 50)
    if i % 2 == 0:
        x.append(i)
        y += 1

print(x)


    