n = int(input('Digite um número de 3 algarismos: '))

c = n // 100
d = (n % 100) // 10 
u = n % 10

print(f'Centena: {c}. Dezena: {d}. Unidade: {u}.')