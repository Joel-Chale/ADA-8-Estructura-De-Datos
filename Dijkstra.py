import heapq

def dijkstra(grafo, inicio):
    # Diccionario para almacenar las distancias mínimas (infinito por defecto)
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    
    # Cola de prioridad para explorar el nodo con menor distancia
    cola_prioridad = [(0, inicio)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si encontramos una distancia mayor a la registrada, la ignoramos
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        # Explorar vecinos
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            # Solo consideramos este camino si es mejor que el anterior
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))
                
    return distancias

# Ejemplo de uso:
grafo_dijkstra = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

origen = 'A'
resultados = dijkstra(grafo_dijkstra, origen)
print("--- Algoritmo de Dijkstra ---")
for nodo, distancia in resultados.items():
    print(f"Distancia mínima de {origen} a {nodo}: {distancia}")