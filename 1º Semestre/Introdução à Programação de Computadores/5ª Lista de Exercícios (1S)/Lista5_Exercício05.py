#Faça um programa que leia um número inteiro positivo N e imprima todos os números
#naturais de 0 até N em ordem decrescente.

N = int(input('Digite um número-> '))

for i in range(N, 0, -1):
    print(i,end=" ")