# Bento Carlos Silva dos Santos RA: 600784
# Fernando Cremonez Costa RA: 604097

coca = input("Mensagem codificada: ").upper()

coca = list(coca)

for i in range(len(coca)):
    try:
        if "P" == coca[i] and coca[i+1] == "P":
            coca.pop(i)
        elif coca[i] == "P":
            coca.pop(i)
    except:
        Exception
    else:
        continue

coca = "".join(coca)
print(coca)
