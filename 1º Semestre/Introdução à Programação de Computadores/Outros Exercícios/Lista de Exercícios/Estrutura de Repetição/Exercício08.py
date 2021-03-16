num = int(input('Digite um número: '))

n = 1
for i in range(num+1):
    for j in range(i):
        print(n, end=' ')
        n += 1
    print()