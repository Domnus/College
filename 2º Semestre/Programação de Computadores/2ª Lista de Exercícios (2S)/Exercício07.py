while True:
    cpf = input("Informe o CPF: ")
    if not(cpf.isdigit()):
        print("CPF inválido, digite apenas números")
    else:
        break
d1 = 0
d2 = 0
for i in range(9):
    d1 += (ord(cpf[i])-48)*(i+1)
    d2 += (ord(cpf[i])-48)*(9-i)
if d1 % 11 == 10:
    d1 = 0
else:
    d1 %= 11
if d2 % 11 == 10:
    d2 = 0
else:
    d2 %= 11

if d1 == int(cpf[9]) and d2 == int(cpf[10]):
    print("CPF válido")
else:
    print("CPF inválido")