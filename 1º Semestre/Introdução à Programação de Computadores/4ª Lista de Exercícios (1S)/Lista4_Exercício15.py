n = int(input('Digite um número: '))

i = 1

while i<=n:
    j = i
    while j<=(i*i):
        print(f'{j}', end=' ')
        j += i
    print()
    i += 1