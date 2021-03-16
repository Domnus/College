palin = 0
for i in range(100,1000):
    for j in range(100,1000):
        num = x = i*j
        inv = 0
        while x > 0:
            inv *= 10
            inv += x % 10
            x //= 10
        if num == inv:
            palin = num
print(palin)