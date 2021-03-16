x = 0
y = 0
z = 0

for i in range(1, 10000):
    x = i // 100
    y = i % 100
    z = x + y
    if (z**2) == i:
        print(i) 
