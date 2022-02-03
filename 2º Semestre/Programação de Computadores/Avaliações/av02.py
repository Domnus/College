# Bento Carlos Silva dos Santos RA: 600784
# Fernando Cremonez Costa RA: 604097

def secToKrunen(sec):
    if sec > 10000:
        minutos = (sec - 10000) // 100
    else:
        minutos = (sec) // 100
    segundos = sec % 100
    horas = sec // 10000

    return horas, minutos, segundos
 
def krunenToSec(h,m,s):
    total = (h*10000) + (m*100) + s

    return total

def krunenToNormal(h,m,s):
    secs = krunenToSec(h,m,s)

    horas = secs // 3600
    minutos = (secs % 3600) // 60
    segundos = (secs % 3600) % 60

    return horas, minutos, segundos

while True:
    print("1. Segundos -> Krunensberg")
    print("2. Krunensberg -> Segundos")
    print("3. Krunenberg -> Nosso Horário")

    x = int(input("-> "))
    if x == 1:
        sec = int(input("Informe os segundos: "))
        if sec > 100000:
            print("Os segundos devem ser menore que 100.000!\n")
            continue
        x = secToKrunen(sec)
        print(f"{x[0]} horas, {x[1]} minutos, {x[2]} segundos.\n")
        
    if x == 2:
        h, m, s = input("Digite no horário de Krunensberg no formato [HH:MM:SS]: ").split(":")
        h = int(h)
        m = int(m)
        s = int(s)
        x = krunenToSec(h, m, s)
        print(f"{x} segundos.\n")
    
    if x == 3:
        h, m, s = input("Digite no horário de Krunensberg no formato [HH:MM:SS]: ").split(":")
        h = int(h)
        m = int(m)
        s = int(s)
        x = krunenToNormal(h, m, s)
        print(f"{x[0]} horas, {x[1]} minutos, {x[2]} segundos.\n")

    else:
        print("Digite uma opção válida!\n")
