def menuPrincipal():
    print("        -----Menu-----")
    print("0. Para o Programa")
    print("1. Decimal para outras bases")
    print("2. Outras bases para decimal")
    print("3. Outras bases para outras bases")
    return int(input("Escolha a opção-> "))

def menu1():
    print("-----Decimal para outras bases-----")
    print("      1. Decimal -> Binário")
    print("      2. Decimal -> Octal")
    print("      3. Decimal -> Hexadecimal")

    op = int(input("Escolha a opção-> "))
    return decimalQBase(op)

def menu2():
    print("-----Outras bases para decimal-----")
    print("     1. Binário -> Decimal")
    print("     2. Octal -> Decimal")
    print("     3. Hexadecimal -> Decimal")

    op = int(input("Escolha a opção-> "))
    return qBaseDecimal(op)

def menu3():
    print("-----Outras bases para outras bases-----")
    print("         1. Binário -> Octal")
    print("         2. Binário -> Hexadecimal")
    print("         3. Octal -> Binário")
    print("         4. Octal -> Hexadecimal")
    print("         5. Hexadecimal -> Binário")
    print("         6. Hexadecimal -> Octal")
    
    op = int(input("Escolha a opção-> "))
    return qBase(op)

def decimalQBase(op):
    n = int(input("Digite o número-> "))
    if op == 1:
        return bin(n)
    elif op == 2: 
        return oct(n)
    elif op == 3: 
        return hex(n)

def qBaseDecimal(op):
    n = input("Digite o número-> ")
    if op == 1:
        return int(n, 2)
    elif op == 2: 
        return int(n, 8)
    elif op == 3:
        return int(n, 16)

def qBase(op):
    n = input("Digite o número-> ")
    if op == 1:
        return oct(int(n, 2))
    elif op == 2: 
        return hex(int(n, 2))
    elif op == 3:
        return bin(int(n, 8))
    elif op == 4:
        return hex(int(n, 8))
    elif op == 5:
        return bin(int(n, 16))
    elif op == 6:
        return oct(int(n, 16))

while True:
    x = menuPrincipal()
    if x == 0:
        break
    elif x == 1:
        print(f"Resultado: {menu1()}")
    elif x == 2:
        print(f"Resultado: {menu2()}")
    elif x == 3:
        print(f"Resultado: {menu3()}")
    else:
        print("Opção inválida!")