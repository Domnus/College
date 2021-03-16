A = int(input('A == '))
B = int(input('B == '))

a = A
b = B 

x = True
while x:
    if B > A:
        print(f'{a} não termina com {b}')
        x = False
    else:
        j = A % 10
        A //= 10
        i = B % 10
        B //= 10
        if j == i or A == 0 and B == 0:
            print(f'{a} termina com {b}')
            x = False
        else:
            print(f'{a} não termina com {b}')
            x = False
        
            
