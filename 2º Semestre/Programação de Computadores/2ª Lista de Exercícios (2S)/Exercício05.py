coca = ["A", "Á", "Ã", "À", "E", "É", "È", "Ẽ", "I", "Í", "Î", "Ĩ", "O", "Ó", "Ò", "Õ", "U", "Ú", "Ù", "Ũ"]

agua = input("Digite uma frase: ").upper()
agua = list(agua)

vogal = 0
consoante = 0

for i in agua:
    if i == " ":
        continue
    elif i in coca:
        vogal += 1
    else:
        consoante += 1

print(f"Código = {(vogal * 5)+(consoante * 10)}")
