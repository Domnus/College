try: 
    f1 = open(input("Nome do 1º arquivo: "), 'r')
    f2 = open(input("Nome do 2º arquivo: "), 'r')
    f3 = open('novo.txt', 'w')
    f3.write(f1.read() + '\n' + f2.read())
    print('Arquivo novo.txt gerado')
    f1.close
    f2.close
    f3.close
except:
    print('Algum dos arquivos não foi encontrado!')
