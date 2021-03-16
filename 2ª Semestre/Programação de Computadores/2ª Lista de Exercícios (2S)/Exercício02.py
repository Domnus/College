palavra = input("Digite uma palavara: ")

for i in range(len(palavra)):
    print(f"{palavra[:(len(palavra)-i)]}")