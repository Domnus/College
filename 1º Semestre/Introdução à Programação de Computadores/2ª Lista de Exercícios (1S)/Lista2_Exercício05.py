a = float(input('Digite o primeiro ângulo do triângulo: '))
b = float(input('Digite o segundo ângulo do triângulo: '))
c = float(input('Digite o terceiro ângulo do triângulo: '))

if (a + b + c) != 180:
    print('Não é um triângulo.')
elif (a < 90) and (b < 90) and (c < 90):
    print('É um triângulo acutângulo.')
elif (a > 90) or (b > 90) or (c > 90):
    print('É um triângulo Obtusângulo.')
else:
    print('É um triângulo retângulo.')