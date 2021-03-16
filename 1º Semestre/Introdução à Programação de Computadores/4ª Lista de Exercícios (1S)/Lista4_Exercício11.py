i = 1000

while i < 10000:
    n1 = i // 100
    n2 = i % 100
    s = n1 + n2
    if s ** 2 == i:
        print(i)
    i += 1    
    

