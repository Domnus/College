# Andressa Caroline R. Bueno RA: 607290
# Bento Carlos S. dos Santos RA: 600784
# Bruno Campos				 RA: 610453
# Frederico Hanai 			 RA: 604593
# Hugo Seiti Odajima 		 RA: 606537
# Paulo Astrauskas 		 	 RA: 548111

from cls import cls
from Grafo import Grafo


def montarGrafoPonderado():
    # vertices = []
    # arestas = []
    # dict_grafo = {}

    # # Input do grafo
    # while not vertices:
    #     vertices = input("Vértices do grafo: ").upper().split()
    #     while True:
    #         res = input("Digite o par de vértices para as arestas [Digite 0 para parar]: ").upper().split()

    #         if res[0] == '0':
    #             break

    #         grau = input("Digite o grau desse vértice: ")

    #         if not grau.isdigit():
    #             print("Grau inválido")
    #             continue
    #         for aresta in res:
    #             if aresta not in vertices:
    #                 arestas.append([res, grau])

    # # Montagem do grafo
    # for vertice in vertices:
    #     dict_grafo[vertice] = {}
    #     arestas_b = {}
    #     for aresta in arestas:
    #         if vertice in aresta[0]:
    #             vertices_adjacentes = list(arestas_b.keys())
    #             vert = [x for x in aresta[0] if x != vertice and x not in vertices_adjacentes]
    #             if len(vert) > 0:
    #                 arestas_b[vert[0]] = aresta[1]
    #                 dict_grafo[vertice] = arestas_b

    #dict_grafo = {
    #   '0': {'1': 6, '2': 1, '3': 5},
    #   '1': {'0': 6, '2': 2, '4': 5},
    #   '2': {'0': 1, '1': 2, '3': 2, '4': 6, '5': 4},
    #   '3': {'0': 5, '2': 2, '5': 4},
    #   '4': {'1': 5, '2': 6, '5': 3},
    #   '5': {'2': 4, '3': 4, '4': 3}
    #}

    #GRAFO PRO DIJKSTRA (V{v:peso}):
    dict_grafo = {
        '1': {'2': 2, '3': 3, '5': 6, '11': 4},
        '2': {'1': 2, '4': 9},
        '3': {'1': 3, '8': 5, '11': 9},
        '4': {'2': 9, '6': 6},
        '5': {'1': 6, '6': 8, '11': 7},
        '6': {'4': 6, '5': 8, '7': 5},
        '7': {'6': 5, '8': 3, '9': 11, '11': 10},
        '8': {'3': 5, '7': 3, '10': 2},
        '9': {'7': 11, '10': 3},
        '10': {'8': 2, '9': 3},
        '11': {'1': 4, '3': 9, '5': 7, '7': 10}
    }
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

        #tipo_grafo = input(">> ")
        tipo_grafo = '1'
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

                vertice_inicial = input("Informe o vértice inicial: ")
                vertice_final = input("Informe o vértice final: ")
                grafo.achar_menor_caminho(vertice_inicial, vertice_final)

                break


        else:
            cls()
            print("------------------------")
            print("Escolha um tipo válido!!")
            print("------------------------")
            continue


if __name__ == "__main__":
    main()
