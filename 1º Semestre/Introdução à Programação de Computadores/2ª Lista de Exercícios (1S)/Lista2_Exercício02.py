num = int(input('Digite um número de 4 algarismo: '))
num1 = ((num % 1000) % 100) % 10

if num > 9999 or num < 1000:
    print("Número inválido. Digite um número de 4 dígitos.")
elif num==1 or num==2:
    print("O dia de rodízio será Segunda-Feira.")
elif num==3 or num==4:
    print("O dia de rodízio será Terça-Feira.")
elif num==5 or num==6:
    print("O dia de rodízio será Quarta-Feira.")
elif num==7 or num==8:
    print("O dia de rodízio será Quinta-Feira.")
else:
    print("O dia de rodízio será Sexta-Feira.")

