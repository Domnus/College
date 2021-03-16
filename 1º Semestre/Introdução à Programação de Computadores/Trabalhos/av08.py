from random import randint

L = []
l = []
for i in range(50):
    L.append(randint(1, 101))
print(L)

print('Digite duas posições da lista: (1 a 50)')

x = True
while x:
        x = int(input('-> '))
        if x > 50 or x < 1:
            print('Número inválido!')
            continue 
        else:
            y = int(input('-> '))
            if y > 50 or y < 1:
                print('Número inválido!')  
                continue
            else:
                if y < x:
                    print('O primeiro número deve ser menor que o segundo!')
                else:
                    for i in range(x-1, y):
                        index = L[i]
                        l.append(index)
                    x = False
    
print(l)


                

