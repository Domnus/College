class Grafo:
    def __init__(self, dicionarioGrafo):
        self.dicionarioGrafo = dicionarioGrafo

    def visualizar(self):
        print(self.dicionarioGrafo)
        return True

    def verticesAdjacentes(self, verticeASerVisualizado):
        print(self.dicionarioGrafo[verticeASerVisualizado])
        return True

    def verificarArestas(self, verticeA, verticeB):
        if( (verticeA in self.dicionarioGrafo[verticeB] ) and (verticeB in self.dicionarioGrafo[verticeA]) ):
            print(f"Vertice ({verticeA}, {verticeB}) tem uma aresta entre eles") 
            return True
        print("Não há arestas entre esses vertices")
        return False

    def calcularGrauDeUmVertice(self, vertice):
        try:
            print(len(self.dicionarioGrafo[vertice]))
            return True
        except:
            return False
        
    def verificarRegularidade(self):
        contador = 0
        for i in self.dicionarioGrafo:
            contador = len(self.dicionarioGrafo[i])
            break
        for i in self.dicionarioGrafo:
            if(contador != len(self.dicionarioGrafo[i])):
                print("O grafo não é regular")
                return False
        print("O grafo é regular")
        return True

grafo = {  'A': ['B', 'C'] ,
          'B': ['A', 'D'],
          'C': ['A', 'D'],
          'D': ['B', 'C'],
          'E': ['D', 'F'],
          'F': ['A', 'E'] } 