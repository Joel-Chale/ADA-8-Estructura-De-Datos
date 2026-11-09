class GrafoKruskal:
    def __init__(self, vertices):
        self.V = vertices # Número de vértices
        self.aristas = [] # Lista de aristas
        
    def agregar_arista(self, u, v, peso):
        self.aristas.append([u, v, peso])
        
    # Función para encontrar el conjunto al que pertenece un elemento (Find)
    def buscar(self, padre, i):
        if padre[i] == i:
            return i
        return self.buscar(padre, padre[i])
        
    # Función para unir dos conjuntos (Union)
    def unir(self, padre, rango, x, y):
        raiz_x = self.buscar(padre, x)
        raiz_y = self.buscar(padre, y)
        
        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    def kruskal(self):
        resultado = [] # Guardará el árbol de expansión mínima
        i = 0 # Índice para las aristas ordenadas
        e = 0 # Contador de aristas en el resultado
        
        # 1. Ordenar todas las aristas de menor a mayor peso
        self.aristas = sorted(self.aristas, key=lambda item: item[2])
        
        padre = []
        rango = []
        
        # Inicializar conjuntos disjuntos
        for nodo in range(self.V):
            padre.append(nodo)
            rango.append(0)
            
        # 2. Agregar aristas hasta tener V-1
        while e < self.V - 1 and i < len(self.aristas):
            u, v, peso = self.aristas[i]
            i = i + 1
            x = self.buscar(padre, u)
            y = self.buscar(padre, v)
            
            # Si incluimos la arista no forma ciclo, se agrega
            if x != y:
                e = e + 1
                resultado.append([u, v, peso])
                self.unir(padre, rango, x, y)
                
        # Imprimir resultado
        print("--- Algoritmo de Kruskal (Árbol de Expansión Mínima) ---")
        costo_total = 0
        for u, v, peso in resultado:
            costo_total += peso
            print(f"Arista: {u} - {v} \tPeso: {peso}")
        print(f"Costo Total del MST: {costo_total}")

# Ejemplo de uso:
# Nodos: 0, 1, 2, 3
g = GrafoKruskal(4)
g.agregar_arista(0, 1, 10)
g.agregar_arista(0, 2, 6)
g.agregar_arista(0, 3, 5)
g.agregar_arista(1, 3, 15)
g.agregar_arista(2, 3, 4)

g.kruskal()