print('-----Quadrado Perfeito-----')
n = int(input('Digite um número-> '))
somaImpares = 0

if n == 1:
    print('Quadrado Perfeito')
else: 
    for impar in range(1, n, 2):
        somaImpares += impar
        if somaImpares == n:
            print('Quadrado Perfeito')
            break
    else:
        print('Não é um quadrado perfeito')
    

   



