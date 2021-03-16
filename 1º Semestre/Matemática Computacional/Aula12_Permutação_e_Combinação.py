from math import factorial

rep = []
fact = 1

C_ou_P = input('Combinação ou Permutação? ').upper()[0]

if C_ou_P == 'C':
    print('-----Combinação-----')
    n = int(input('-> '))
    r = int(input('-> '))
    C = factorial(n) / (factorial(r) * factorial(n - r))
elif C_ou_P == 'P':
    print('-----Permutação-----')
    n = int(input('-> '))
    r = int(input('-> '))
    if n > r:
        C = factorial(n) / factorial(n - r)
    elif n == r:
        rep = input('Insira o número de repetições de elementos, separados por um espaço: ').split()
        for i in range(len(rep)):
          rep[i] = int(rep[i])
        for i in rep:
          fact *= factorial(i)
          C = factorial(n) / fact         

print(C)

