def media_digitos(n):
    media = list(int(digit) for digit in str(n))
    return sum(media) / len(media)

x = int(input("Digite um número: "))
print(f"A média dos dígites é {media_digitos(x)}.")

