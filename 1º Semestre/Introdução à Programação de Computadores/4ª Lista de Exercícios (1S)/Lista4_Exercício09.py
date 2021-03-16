length = int(input('Quantos números deseja? '))
x = 1
y = 1
i = 3

print(f'{x} {y}', end=' ')
while i <= length:
    z = x + y
    print(z, end=' ')
    x = y
    y = z
    i += 1
    
    

    