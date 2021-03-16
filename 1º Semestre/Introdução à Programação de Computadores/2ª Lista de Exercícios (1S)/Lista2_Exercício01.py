num = int(input('Digite um número de no máximo 3 algarismo: '))

if num < 1000 and num > 99:
    num1 = num // 100
    num2 = (num // 10) % 10
    num3 = (num % 10)
    if num1 < num2 < num3:
        print('O número é ascendente.')
    else:
        print('O número não é ascendente.')
        


