def comb(n, k):
    if k > n:
        return 0
    if k == 1:
        return n
    if k == n:
        return 1
    
    return comb(n-1,k-1) + comb(n-1, k)


A, B = input("Informe os números para o cálculo dos grupos no formato [N K]: ").split(' ')

print(f"É possível montar {comb(int(A), int(B))} grupos diferentes.")
