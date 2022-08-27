# Bento Carlos S. dos Santos RA: 600784
# Hugo Seiti Odajima 		   RA: 606537
# Paulo Guilherme Astrauskas RA: 548111

from Pessoa import Pessoa
from Cartao import Cartao
from Compra import Compra
from Maquininha import Maquininha

def main():
    pessoa = Pessoa("Rodrigo Faro", "rodrigofaro@record.com", "123456789", "11 99999-9999", 30)
    cartao = Cartao("Rodrigo Faro", '000000000000', "VISA", 1234, 15000)
    compra = Compra(pessoa, "01/01/2019", 100)

    moderninha = Maquininha(cartao, compra.getValor(), 1234)
    moderninha.validar()


if __name__ == "__main__":
    main()