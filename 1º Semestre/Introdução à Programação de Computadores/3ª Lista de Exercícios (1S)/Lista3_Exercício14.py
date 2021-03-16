from random import randint
print("Vovô Alcindo, informe 2 bichos para a aposta")
b1 = int(input("1º bicho (1 a 25) -> "))
b2 = int(input("2º bicho (1 a 25) -> "))
if 1<=b1<=25 and 1<=b2<=25:
    m1 = randint(0,9999)
    g1 = (m1-1) % 100 // 4 + 1
    m2 = randint(0,9999)
    g2 = (m2-1) % 100 // 4 + 1
    m3 = randint(0,9999)
    g3 = (m3-1) % 100 // 4 + 1
    m4 = randint(0,9999)
    g4 = (m4-1) % 100 // 4 + 1
    m5 = randint(0,9999)
    g5 = (m5-1) % 100 // 4 + 1
    print("Prêmio  Milhar  Grupo")
    print("  1º     {:04}     {:2}".format(m1, g1))
    print("  2º     {:04}     {:2}".format(m2, g2))
    print("  3º     {:04}     {:2}".format(m3, g3))
    print("  4º     {:04}     {:2}".format(m4, g4))
    print("  5º     {:04}     {:2}".format(m5, g5))
    if b1 in [g1,g2,g3,g4,g5] and b2 in [g1,g2,g3,g4,g5]:
        print("Vovô Alcindo, o senhor ganhou no jogo do bicho :)")
    else:
        print("Não foi dessa vez vovô Alcindo :(")
else:
    print("Algum bicho apostado está inválido!!")