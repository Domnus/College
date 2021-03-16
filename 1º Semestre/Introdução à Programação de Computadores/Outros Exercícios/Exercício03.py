n = int(input('Digite um número-> '))

bin = True
while n > 0:
    s = n % 10
    n //= 10
    if s > 1:
        bin = False
        break

if bin:
    print('Número binário')
else: 
    print('Número não binário')
    
    