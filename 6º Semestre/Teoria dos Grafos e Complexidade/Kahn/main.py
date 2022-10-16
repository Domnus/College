# Andressa Caroline R. Bueno RA: 607290
# Bento Carlos S. dos Santos RA: 600784
# Bruno Campos				 RA: 610453
# Frederico Hanai 			 RA: 604593
# Hugo Seiti Odajima 		 RA: 606537
# Paulo Astrauskas 		 	 RA: 548111

from cls import cls
from Grafo import Grafo


def montarGrafoPonderado():
    #vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    #arestas = [
    #    [['A', 'B'], 5 ],
    #    [['A', 'D'], 12],
    #    [['B', 'A'], 5 ],
    #    [['B', 'D'], 3 ],
    #    [['B', 'C'], 2 ],
    #    [['B', 'F'], 10],
    #    [['C', 'B'], 2 ],
    #    [['C', 'E'], 8 ],
    #    [['C', 'F'], 3 ],
    #    [['D', 'A'], 12],
    #    [['D', 'B'], 3 ],
    #    [['D', 'E'], 4 ],
    #    [['E', 'C'], 8 ],
    #    [['E', 'D'], 4 ],
    #    [['E', 'D'], 4 ],
    #    [['E', 'F'], 6 ],
    #    [['F', 'B'], 10],
    #    [['F', 'C'], 3 ],
    #    [['F', 'E'], 6 ]
    #]
    #vertices = []
    #arestas = []
    #dictGrafo = {}

	# Input do grafo
	#while vertices == []:
	#	vertices = input("Vértices do grafo: ").upper().split()
	#	while True:
	#		res = input("Digite o par de vértices para as arestas [Digite 0 para parar]: ").upper().split()

	#		if res[0] == '0':
	#			break
	#
	#		grau = input("Digite o grau desse vértice: ")
	#
	#		if not grau.isdigit():
	#			print("Grau inválido")
	#			continue
	#
	#		for aresta in res:
	#			if aresta not in vertices:
	#		{'A': {'B': '5', 'D': '12'}, 'B': {'A': '5', 'D': '3', 'C': '2', 'F': '10'}, 'C': {'B': '2', 'E': '8', 'F': '3'}, 'D': {'A': '12', 'B': '3', 'E': '4'}, 'E': {'C': '8', 'D': '4', 'F': '6'}, 'F': {'B': '10', 'C': '3', 'E': '6'}}	arestas.append([res, grau])

	# Montagem do grafo
    #for vertice in vertices:
    #    dictGrafo[vertice] = {}
    #    arestasB = {}
    #    for aresta in arestas:
    #        if vertice in aresta[0]:
    #            verticesAdjacentes = list(arestasB.keys())
    #            vert = [x for x in aresta[0] if x != vertice and x not in verticesAdjacentes]
    #            if len(vert) > 0:
    #                arestasB[vert[0]] = aresta[1]
    #                dictGrafo[vertice] = arestasB


    #dictGrafo = {
    #    '0': {'1': 6, '2': 1, '3': 5},
    #    '1': {'0': 6, '2': 2, '4': 5},
    #    '2': {'0': 1, '1': 2, '3': 2, '4': 6, '5': 4},
    #    '3': {'0': 5, '2': 2, '5': 4},
    #    '4': {'1': 5, '2': 6, '5': 3},
    #    '5': {'2': 4, '3': 4, '4': 3}
    #}
    dictGrafo = {
            'A': {'B': 5, 'D': 12},
            'B': {'A': 5, 'D': 3, 'C': 2, 'F': 10},
            'C': {'B': 2, 'E': 8, 'F': 3},
            'D': {'A': 12, 'B': 3, 'E': 4},
            'E': {'C': 8, 'D': 4, 'F': 6},
            'F': {'B': 10, 'C': 3, 'E': 6}
    }
    return Grafo(dictGrafo)


def montarGrafoDirecionado():
    # vertices = ['V1', 'V2', 'V3', 'V4']
    # arestas = [['V1', 'V2'], ['V2', 'V3'], ['V3', 'V1'], ['V4', 'V1']]
    vertices = []
    arestas = []
    dictGrafo = {}

    while vertices == []:
        vertices = input("Vértices do grafo: ").upper().split()

    while True:
        res = input("Digite o par de vértices para as arestas [Digite 0 para parar]: ").upper().split()
        if res[0] == '0':
            break

        for aresta in res:
            if aresta not in vertices:
                print("Aresta inválida")
                continue
        arestas.append(res)

    for vertice in vertices:
        dictGrafo[vertice] = {}
        arestasB = []
        for aresta in arestas:
            if vertice == aresta[0]:
                vert = [x for x in aresta if x != vertice and x not in arestasB]
                if len(vert) > 0:
                    arestasB.append(vert[0])
        dictGrafo[vertice] = arestasB

    # dictGrafo = {
    #	"A":["B","E"],
    #	"B":["C","F","H"],
    #	"C":[],
    #	"D":["B"],
    #	"E":["F"],
    #	"F":[],
    #	"G":["E","H"],
    #	"H":[]
    # }

    return Grafo(dictGrafo)


def montarGrafoNaoDirecionado():
    # vertices = []
    # while vertices == []:
    #	vertices = input("Vértices do grafo: ").upper().split()
    # arestas = []
    # while True:
    #	res = input("Digite o par de vértices para as arestas [Digite 0 para parar]: ").upper().split()
    #	if res[0] == '0':
    #		break

    #	for aresta in res:
    #		if aresta not in vertices:
    #			print("Aresta inválida")
    #			continue
    #	arestas.append(res)

    # dictGrafo = {}

    # for vertice in vertices:
    #	dictGrafo[vertice] = {}
    #	arestasB = []
    #	for aresta in arestas:
    #		if vertice in aresta:
    #			vert = [x for x in aresta if x != vertice and x not in arestasB]
    #			if len(vert) > 0:
    #				arestasB.append(vert[0])
    #	dictGrafo[vertice] = arestasB

    dictGrafo = {
        'V1': ['V2', 'V3'],
        'V2': ['V1', 'V3'],
        'V3': ['V1', 'V2', 'V4'],
        'V4': ['V3']
    }

    return Grafo(dictGrafo, True)


def montarGrafo(tipoGrafo):
    if tipoGrafo == "1":
        grafo = montarGrafoPonderado()  # TODO: montar o input do grafo ponderado
    elif tipoGrafo == "2":
        grafo = montarGrafoDirecionado()  # TODO: montar o input do grafo direcionado
    elif tipoGrafo == "3":
        grafo = montarGrafoNaoDirecionado()
    else:
        grafo = None

    # dictGrafo = {
    #	"A":["B","C"],
    #	"B":["F"],
    #	"C":["F"],
    #	"D":["C","E"],
    #	"E":["C","F"],
    #	"F":[]
    # }

    return grafo


def main():
    while True:
        print("Escolha o tipo de grafo: ")
        print("[1] Grafo ponderado")
        print("[2] Grafo direcionado")
        print("[3] Grafo não-direcionado")
        print("[0] Sair")

        #tipoGrafo = iagm = {}nput(">> ")
        tipoGrafo = '1'
        if tipoGrafo.isnumeric():
            if tipoGrafo == '0':
                break
            else:
                grafo = montarGrafo(tipoGrafo)
                if grafo is None:
                    cls()
                    print("-----------------------")
                    print("Essa opção não existe!!")
                    print("-----------------------")
                    continue
                grafoAGM = grafo.kruskal()

                if grafoAGM is not None:
                    for vertice in grafoAGM.dictGrafo:
                        print(f"{vertice}: {grafoAGM.dictGrafo[vertice]}")
                break
        else:
            cls()
            print("------------------------")
            print("Escolha um tipo válido!!")
            print("------------------------")
            continue


if __name__ == "__main__":
    main()
