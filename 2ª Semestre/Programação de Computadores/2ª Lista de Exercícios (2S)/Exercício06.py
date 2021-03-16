frase = input("String: ").upper()
coca = frase.strip(",.")

latao = list(coca)

for i in range(len(latao)):
    if latao[i] == " ":
        continue
    if latao[i] == "X":
        latao[i] = "A"
    elif latao[i] == "Y":
        latao[i] = "B"
    elif latao[i] == "Z":
        latao[i] = "Z"
    else:
        agua = ord(latao[i])
        latao[i] = chr(agua + 3)

meri = "".join(latao)

print(meri)

    
