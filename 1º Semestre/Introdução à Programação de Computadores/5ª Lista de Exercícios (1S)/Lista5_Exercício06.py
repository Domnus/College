# Em Matemática, um número harmônico designado por H(n) define-se como sendo a soma
# da série harmônica: H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n Faça um programa que leia um
# valor n inteiro e positivo e apresente o valor de H(n).

N = int(input('Digite um número-> '))
SH = 0

for i in range(1, N+1):
    SH += 1/i
     
print(f'O resultado da série harmônica será {SH:.6f}')