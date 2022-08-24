from random import randint
from time import sleep
from Processo import Processo
from datetime import datetime
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def tempo_execucao():
	return randint(1, 10) * 5


def prioridade():
	return randint(1, 5)


def printao(pilha, time_slice):
	cls()
	print("|-------------------------------------------------------------|")
	print("| Process ID | Tempo Entrada | Tempo de Execução | Prioridade |")
	for item in pilha:
		print("|------------+---------------+-------------------+------------|")
		print(f"|{item.id:^12}", end="")
		tempo_entrada = item.tempo_entrada.strftime("%H:%M:%S")
		print(f"|{tempo_entrada:^15}", end="")
		print(f"|{item.tempo_execucao:^19}", end="")
		print(f"| {item.prioridade:^11}|")
	print("|-------------------------------------------------------------|")
	print(f"Time Slice: {time_slice}		CPU: [{pilha[0].id}]")
	

if __name__ == "__main__":
	pilha = []
	contadorId = 1
	time_slice = 5
	while True:
		res = input("Deseja adicionar um processo? (s/n) ").lower()[0]
		if res == 's':
			pilha.append(Processo(contadorId, datetime.now(), tempo_execucao(), prioridade()))
			contadorId += 1
		elif res == 'n':
			pass
		else: 
			print("Opção inválida!")
			continue

		if len(pilha) > 0:
			pilha.sort(key=lambda x: (x.prioridade, x.tempo_entrada), reverse=True)
			printao(pilha, time_slice)

			if pilha[0].prioridade > 1:
				pilha[0].prioridade -= 1

			pilha[0].tempo_execucao -= time_slice
			if pilha[0].tempo_execucao <= 0:
				pilha.pop(0)

			pilha.sort(key=lambda x: (x.prioridade, x.tempo_entrada), reverse=True)
		else:
			print("Todos os processos foram executados.")
			break
		sleep(1)