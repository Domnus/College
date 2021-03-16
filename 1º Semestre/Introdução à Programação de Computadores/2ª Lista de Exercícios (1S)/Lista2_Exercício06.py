a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))

if a > b:
    a, b = b,a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
    

print(a,b,c)

#if a > b and a > c:
#    if b > c:
#        print(c,b,a)
#    elif c > b:
#        print(b,c,a)
#elif b > a and b > c:
#    if a > c:
#        print(c,a,b)
#    else:
#        print(a,c,b)
#else:
#    if a > b:
#        print(b,a,c)
#    else:
#        print(a,b,c)

    