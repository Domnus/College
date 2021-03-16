from random import randint

L = []
l = []

for i in range(20):
    L.append(randint(1, 50))
print(L)

x = int(input('Digite o número o qual deseja os múltiplos ->  '))

for j in L:
    if j % x == 0:
        l.append(j)
    
if l == []:
        print(f'Não há números divisíveis por {x} nessa lista.')
else:
    print(f'Os números divisíveis por {x} são: {l}')        
      



