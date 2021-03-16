numeros = []
pares = []
soma = 0
somaPares = 0

print('Digite os números\nDigite 0 para parar o programa')
while True:
    n = int(input('-> '))
    if n == 0:
        break
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)

numeros.sort()
for i in numeros:
    soma += i

for i in pares:
    somaPares += i

quantidadeNumeros = len(numeros)
media = soma / quantidadeNumeros
maior = numeros[-1]
menor = numeros[0]
mediaPares = somaPares / (len(pares))

print(f'Soma dos números digitados: {soma}')
print(f'Quantidade de números digitados: {quantidadeNumeros}')
print(f'Média dos números digitados: {media}') 
print(f'Maior número digitado: {maior}')
print(f'Menor número digitado: {menor}')
print(f'Média dos pares: {mediaPares}')
    