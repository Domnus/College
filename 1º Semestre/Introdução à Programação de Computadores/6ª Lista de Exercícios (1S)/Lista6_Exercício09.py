from random import randint

L = []
i = 0

while i < (10):    
    x = randint(1, 50)
    if x not in L:
        L.append(x)
        i += 1    
print(L)