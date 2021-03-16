A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))

soma = 0

if (A % 2) == 1:
    while A <= B:
        soma += A
        A += 2
else:
    A += 1
    while A <=B:
        soma += A
        A += 2
        
print(soma)



