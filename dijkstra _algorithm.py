import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm for finding the shortest path in a graph.
    Parameters:
    - graph (dict): A dictionary representing the graph where the keys are vertices and the values are dictionaries
                    containing the neighbors and their corresponding edge weights.
    - start (object): The starting vertex for the algorithm.
    Returns:
    - distances (dict): A dictionary containing the shortest distances from the starting vertex to all other vertices
                        in the graph.
    """
    # Priority queue to store (distance, vertex)
    pq = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(f"Distances from {start_vertex}: {distances}")
