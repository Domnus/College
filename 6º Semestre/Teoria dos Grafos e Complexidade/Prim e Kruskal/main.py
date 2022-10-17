# Andressa Caroline R. Bueno RA: 607290
# Bento Carlos S. dos Santos RA: 600784
# Bruno Campos				 RA: 610453
# Frederico Hanai 			 RA: 604593
# Hugo Seiti Odajima 		 RA: 606537
# Paulo Astrauskas 		 	 RA: 548111

from cls import cls
from Grafo import Grafo


def montarGrafoPonderado():
    vertices = []
    arestas = []
    dict_grafo = {}

    # Input do grafo
    while not vertices:
        vertices = input("Vértices do grafo: ").upper().split()
        while True:
            res = input("Digite o par de vértices para as arestas [Digite 0 para parar]: ").upper().split()

            if res[0] == '0':
                break

            grau = input("Digite o grau desse vértice: ")

            if not grau.isdigit():
                print("Grau inválido")
                continue
            for aresta in res:
                if aresta not in vertices:
                    arestas.append([res, grau])

    # Montagem do grafo
    for vertice in vertices:
        dict_grafo[vertice] = {}
        arestas_b = {}
        for aresta in arestas:
            if vertice in aresta[0]:
                vertices_adjacentes = list(arestas_b.keys())
                vert = [x for x in aresta[0] if x != vertice and x not in vertices_adjacentes]
                if len(vert) > 0:
                    arestas_b[vert[0]] = aresta[1]
                    dict_grafo[vertice] = arestas_b
    return Grafo(dict_grafo)


def montarGrafoDirecionado():
    vertices = []
    arestas = []
    dict_grafo = {}

    while not vertices:
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
        dict_grafo[vertice] = {}
        arestas_b = []
        for aresta in arestas:
            if vertice == aresta[0]:
                vert = [x for x in aresta if x != vertice and x not in arestas_b]
                if len(vert) > 0:
                    arestas_b.append(vert[0])
        dict_grafo[vertice] = arestas_b

    return Grafo(dict_grafo)


def montarGrafoNaoDirecionado():
    vertices = []
    while not vertices:
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

    dict_grafo = {}

    for vertice in vertices:
        dict_grafo[vertice] = {}
        arestas_b = []
        for aresta in arestas:
            if vertice in aresta:
                vert = [x for x in aresta if x != vertice and x not in arestas_b]
                if len(vert) > 0:
                    arestas_b.append(vert[0])
        dict_grafo[vertice] = arestas_b

    dict_grafo = {
        'V1': ['V2', 'V3'],
        'V2': ['V1', 'V3'],
        'V3': ['V1', 'V2', 'V4'],
        'V4': ['V3']
    }

    return Grafo(dict_grafo, True)


def montarGrafo(tipo_grafo):
    if tipo_grafo == "1":
        grafo = montarGrafoPonderado()  # TODO: montar o input do grafo ponderado
    elif tipo_grafo == "2":
        grafo = montarGrafoDirecionado()  # TODO: montar o input do grafo direcionado
    elif tipo_grafo == "3":
        grafo = montarGrafoNaoDirecionado()
    else:
        grafo = None

    return grafo


def main():
    while True:
        print("Escolha o tipo de grafo: ")
        print("[1] Grafo ponderado")
        print("[2] Grafo direcionado")
        print("[3] Grafo não-direcionado")
        print("[0] Sair")

        tipo_grafo = input(">> ")
        if tipo_grafo.isnumeric():
            if tipo_grafo == '0':
                break
            else:
                grafo = montarGrafo(tipo_grafo)
                if grafo is None:
                    cls()
                    print("-----------------------")
                    print("Essa opção não existe!!")
                    print("-----------------------")
                    continue
                grafo_agm = grafo.kruskal()

                if grafo_agm is not None:
                    for vertice in grafo_agm.dictGrafo:
                        print(f"{vertice}: {grafo_agm.dictGrafo[vertice]}")
                break
        else:
            cls()
            print("------------------------")
            print("Escolha um tipo válido!!")
            print("------------------------")
            continue


if __name__ == "__main__":
    main()
