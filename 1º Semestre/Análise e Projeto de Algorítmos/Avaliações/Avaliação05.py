c = True
x = 100

while c:
    num1 = x // 100
    num2 = (x // 10) % 10
    num3 = (x % 10)
    if num1 < num2 < num3:
        print(f'O número {x} é ascendente.')
    x += 1
    c = x < 1000


