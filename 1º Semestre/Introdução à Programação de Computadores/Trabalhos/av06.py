i = 1
n = 1
cont = 0
x = True
while x:
    while i <= 15:
        if n % i == 0:
            cont += 1
            i += 1
        else:
            n += 1
            i = 1
            cont = 0
    if cont == 15:
        x = False

print(n)
