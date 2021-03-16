print('-----Sequência de Fibonacci-----')
n = int(input('Digite um número-> '))

x = 1
y = 0

for i in range(1, n+1):
    z = x + y
    print(z, end=' ')
    x = y
    y = z
    