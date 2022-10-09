# Andressa Caroline R. Bueno RA: 607290
# Bento Carlos S. dos Santos RA: 600784
# Bruno Campos				 RA: 610453
# Frederico Hanai 			 RA: 604593
# Hugo Seiti Odajima 		 RA: 606537
# Paulo Astrauskas 		 	 RA: 548111

from threading import Thread, Semaphore, Lock
from time import sleep

sem = Lock()

saldoArquivo = 1000

def Deposito(valor):
	global saldoArquivo
	with sem:
		saldoArquivo += valor
		print("Deposito: ", saldoArquivo)
		sleep(.5)


def Saque(valor):
	global saldoArquivo
	with sem:
		saldoArquivo -= valor
		print("Saque: ", saldoArquivo)
		sleep(.5)


while True:
	caixa1 = Thread(target = Saque(200)).start()
	caixa2 = Thread(target = Deposito(300)).start()
