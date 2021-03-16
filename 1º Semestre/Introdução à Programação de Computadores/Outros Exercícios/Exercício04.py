for i in range(100, 1000):
  c = i // 100
  d = (i % 10) // 10
  u = i % 10
  if (i % 2) == 0:
    
    soma = c + d + u
    print(i, end = " - ")
    print(soma)
  else:
    
    soma = c * d * u
    print(i, end = " - ")
    print(soma)