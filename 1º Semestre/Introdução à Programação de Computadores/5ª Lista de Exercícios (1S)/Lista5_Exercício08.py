# Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2
# fornecidos pelo usuário via teclado. O programa fica pedindo estes valores e calculando até
# que o usuário entre com um valor para resistência igual a zero.

x = True

print('-----Digite 0 para parar o programa-----')

while x:
    R1 = int(input('Digite o valor do primeiro resistor-> '))
    if R1 == 0:
        print('-----Programa parado pelo usuário.-----')
        x = False
    else:
        R2 = int(input('Digite o valor do segundo resistor-> '))
        if R2 == 0:
            print('-----Programa parado pelo usuário.-----')
            x = False
        else:
            r = ((R1*R2) / (R1+R2))
            print(f"O resultado da associação em paralelo é igual a {r:.4f}Ω")

