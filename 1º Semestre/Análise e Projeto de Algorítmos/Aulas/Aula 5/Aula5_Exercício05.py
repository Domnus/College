l1 = float(input("Digite o primeiro lado do triângulo: "))
l2 = float(input("Digite o segundo lado do triângulo: "))
l3 = float(input("Digite o terceiro lado do triângulo: "))

if (l1 +l2) < l3 or (l1 + l3) < l2 or (l2 + l3) < l1:
    print('Não é um triângulo.')
elif l1==l2 and l2==l3:
    print("É um triângulo equilátero.")
elif l1==l2 or l1==l3 or l2==l3:
    print("É um triângulo isósceles.")
else:
    print("É um triângulo escaleno.")