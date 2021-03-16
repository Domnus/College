num = int(input('Digite um número-> '))
inv = 0

while num > 0:
    inv *= 10
    inv += num % 10
    num //= 10  
    
print(inv)


    

