c = True
n = int(input('Digite um número: '))
i = 0


while c:
    n //= 10
    i += 1
    c = n > 0

print(i)


