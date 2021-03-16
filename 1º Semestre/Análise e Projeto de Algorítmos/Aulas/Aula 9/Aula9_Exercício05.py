massaInicial = float(input('Digite a massa do material-> '))
massaFinal = massaInicial
x = True
t = 0

while x:
    massaFinal = massaFinal / 2
    t += 50
    if massaFinal <= 0.5:
        break

h = t // 3600
m = (t % 3600) // 60
s = (t % 3600) % 60

print(f'Massa inicial: {massaInicial}. \nMassa final: {massaFinal}. \nTempo: {h} horas, {m} minutos e {s} segundos.')