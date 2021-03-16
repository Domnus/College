def mdc(x, y):
    if y <= x and x % y == 0:
        return y
    if x < y:
        return mdc(y, x)
    return mdc(y, x%y)

A, B = input("Informe os números para o cálculo do MDC no formato [N N]: ").split(' ')

print(f"O MDC será {mdc(int(A), int(B))}")