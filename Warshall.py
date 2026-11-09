def algoritmo_warshall(matriz):
    V = len(matriz)
    # Copia de la matriz (1 significa hay camino, 0 no hay camino)
    alcanzabilidad = [[matriz[i][j] for j in range(V)] for i in range(V)]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Operación lógica: i alcanza a j si ya lo alcanzaba, 
                # o si i alcanza a k Y k alcanza a j
                alcanzabilidad[i][j] = alcanzabilidad[i][j] or (alcanzabilidad[i][k] and alcanzabilidad[k][j])
                
    return alcanzabilidad

# Ejemplo de uso (1 = conectado, 0 = desconectado):
grafo_warshall = [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

resultado_warshall = algoritmo_warshall(grafo_warshall)
print("--- Algoritmo de Warshall (Cierre Transitivo) ---")
print("Matriz de alcanzabilidad:")
for fila in resultado_warshall:
    print(fila)