meri = input('Digite a frase desejada: ')

meri = list(meri)

if len(meri) % 2 == 0:
    coca = (len(meri) // 2) - 1
    latao = (len(meri)) // 2 
    print(f"{meri[coca]}{meri[latao]}")
else:
    coca = len(meri) / 2
    print(f"{meri[int(coca)]}")
