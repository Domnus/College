t = int(input('Segundos: '))

h = t // 3600
m = (t % 3600) // 60
s = (t % 3600) % 60

print(f'{h} horas, {m} minutos, {s} segundos.')