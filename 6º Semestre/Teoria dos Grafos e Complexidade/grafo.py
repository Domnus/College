# Andressa Caroline R. Bueno RA: 607290
# Bento Carlos S. dos Santos RA: 600784
# Bruno Campos				 RA: 610453
# Frederico Hanai 			 RA: 604593
# Hugo Seiti Odajima 		 RA: 606537
# Paulo Astrauskas 		 	 RA: 548111

import os
from random import randint

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


class Grafo:
	def __init__(self, dictGrafo = None):
		if dictGrafo == None:
			dictGrafo = {}
		else:
			self.dictGrafo = dictGrafo


	def get_vertices(self):
		return list(self.dictGrafo.keys())


	def get_arestas(self):
		return list(self.dictGrafo.values())


	def verticeAleatorio(self):
		vertices = self.get_vertices()
		return randint(0, len(vertices) - 1)


	def find_path(self, vertice_inicial, vertice_final, path=[]):
		grafo = self.dictGrafo
		path = path + [vertice_inicial]
		if vertice_inicial == vertice_final:
			return [path]
		if vertice_inicial not in grafo:
			return []
		paths = []
		for vertex in grafo[vertice_inicial]:
			if vertex not in path:
				extended_paths = self.find_path(vertex, vertice_final, path)
				for p in extended_paths: 
					paths.append(p)
		return paths

	def busca_profunda(self):
		visitados = []
		pilha = []

		vertices = self.get_vertices()
		verticeAleatorio = self.verticeAleatorio()

		pilha.append(vertices[verticeAleatorio])
		visitados.append(vertices[verticeAleatorio])

		while len(pilha) > 0:
			cls()
			vertA = pilha.pop()

			print(f"Vértice atual: {vertA}")
			print(f"Pilha: {pilha}")
			print(f"Visitados: {visitados}")

			input("Pressione ENTER para continuar...")

			for vertB in self.dictGrafo[vertA]:
				if vertB not in visitados:
					visitados.append(vertB)
					pilha.append(vertA)
					pilha.append(vertB)
					
					break


	def verificar_ciclo(self, vertice, visitados, primeiroVertice, caminho = []):
		visitados.append(vertice)
		caminho.append(vertice)
		caminhoAchado = False
		for verticeAdjacente in self.dictGrafo[vertice]:
			if caminhoAchado:
				return [caminho, True]
			if verticeAdjacente not in visitados:
				caminho = self.verificar_ciclo(verticeAdjacente, visitados, vertice, caminho)
				if caminho == None:
					return [caminho, False]
				if caminho[1]:
					caminhoAchado = True
					return [caminho[0], True]
			elif primeiroVertice != verticeAdjacente:
				caminho.append(verticeAdjacente)
				caminhoAchado = True


	def achar_ciclo(self):
		vertices = self.get_vertices()
		visitados = []

		for vertice in vertices:
			if vertice not in visitados:
				caminho = self.verificar_ciclo(vertice, visitados, vertice)
				if caminho[1]:
					print("Ciclo achado no grafo: ", caminho[0])
					break

	def verticeSeguro(self, vertices):
		grafo = self.dictGrafo

		#for
		#TODO: fazer a função que verifica se o vértice é seguro


	def montarAGM(self):
		grafo = self.dictGrafo
		#verticeAleatorio = self.verticeAleatorio()
		verticeAleatorio = '0'

		for verticeAdjacente in grafo[verticeAleatorio]:
			verticeSeguro = self.verticeSeguro(verticeAdjacente)

			#if verticeSeguro:
			#TODO: fazer a função que monta a AGM


	def validarConexo(self):
		grafo = self.dictGrafo
		arestas = grafo.get_arestas()
		contador = 0

		for aresta in arestas:
			if len(aresta) == 0:
				contador += 1

		if len(arestas) == contador:
			print("O grafo não tem arestas")
			return False 

		vertices = grafo.get_vertices()
		for vertA in vertices:
			for vertB in vertices:
				caminhos = grafo.find_path(vertA, vertB)
				caminhos.sort(key = len)

				if len(caminhos) == 0:
					return False

		return True

def montarGrafo(ponderado):
	if ponderado:
		#TODO: montar o input do grafo ponderado
		pass
	else:
		vertices = []
		while vertices == []:
			vertices = input("Vértices do grafo: ").upper().split()
		arestas = []
		while True:
			res = input("Digite o par de vértices para as arestas [Digite 0 para parar]: ").upper().split()
			if res[0] == '0':
				break

			for aresta in res:
				if aresta not in vertices:
					print("Aresta inválida")
					continue
			arestas.append(res)

		dictGrafo = {}

		for vertice in vertices:
			dictGrafo[vertice] = {}
			arestasB = []
			for aresta in arestas:
				if vertice in aresta:
					vert = [x for x in aresta if x != vertice and x not in arestasB]
					if len(vert) > 0:
						arestasB.append(vert[0])
			dictGrafo[vertice] = arestasB

	#dictGrafo = {
	#	'A': ['B', 'D', 'E'],
	#	'B': ['A', 'C'],
	#	'C': ['B', 'F'],
	#	'D': ['A', 'E', 'G'],
	#	'E': ['A', 'B', 'D'],
	#	'F': ['C', 'H', 'I'],
	#	'G': ['D', 'H'],
	#	'H': ['F', 'G', 'I'],
	#	'I': ['F', 'H'],
	#}

	dictGrafo = {
		'0': {'1': 6, '2': 1, '3': 5},
		'1': {'0': 6, '2': 2, '4': 5},
		'2': {'0': 1, '1': 2, '3': 2, '4': 6, '5': 4},
		'3': {'0': 5, '2': 2, '5': 4},
		'4': {'1': 5, '2': 6, '5': 3},
		'5': {'2': 4, '3': 4, '4': 3}
	}

	return Grafo(dictGrafo)


def main():
	while True:
		tipoGrafo = input("É um grafo ponderado? [S/N] ): ").upper()[0]

		if tipoGrafo == "S":
			grafo = montarGrafo(True)
			break
		elif tipoGrafo == "N":
			grafo = montarGrafo(False)
			break
		else:
			print("Resposta inválida")


	#dictGrafo = {
	#	'V1': ['V2', 'V3'],
	#	'V2': ['V1', 'V3'],
	#	'V3': ['V1', 'V2', 'V4'],
	#	'V4': ['V3']
	#}


	grafo.montarAGM()

if __name__== "__main__":
	main()