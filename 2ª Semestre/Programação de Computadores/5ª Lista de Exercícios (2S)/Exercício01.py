def elevar(numero, expoente):
    if expoente == 0:
        return 1
    return numero * elevar(numero, expoente - 1) 

numero, expoente = input("Digite o número e o expoente no format [N N]: ").split(" ")
numero = int(numero)
expoente = int(expoente)

print(f"{numero} elevado a {expoente} é igual a {elevar(numero, expoente)}")