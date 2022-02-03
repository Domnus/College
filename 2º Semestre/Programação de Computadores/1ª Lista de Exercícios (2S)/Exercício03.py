frase = input("Digite uma frase: ")
c1 = input('Primeiro caractere: ')
c2 = input('Segundo caractere: ')
cont = frase.count(c1)
frase = frase.replace(c1,c2)
cont = frase.count(c2)

print(f'O caractere {c1} foi substituído {cont} vezes')
