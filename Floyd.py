INF = float('inf')

def algoritmo_floyd(matriz):
    # Número de vértices
    V = len(matriz)
    
    # Crear una copia de la matriz para no modificar la original
    dist = [[matriz[i][j] for j in range(V)] for i in range(V)]
    
    # Agregar todos los vértices uno por uno al conjunto de vértices intermedios
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Si el camino pasando por k es más corto, se actualiza
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist

# Ejemplo de uso (Matriz de adyacencia):
# Nodos: 0, 1, 2, 3
grafo_floyd = [
    [0,   5,  INF, 10],
    [INF, 0,   3,  INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

resultado_floyd = algoritmo_floyd(grafo_floyd)
print("--- Algoritmo de Floyd ---")
print("Matriz de distancias más cortas entre todos los pares:")
for fila in resultado_floyd:
    print(fila)