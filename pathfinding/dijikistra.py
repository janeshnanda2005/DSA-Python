import heapq
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2},
    'C': {'B': 1, 'D': 6},
    'D': {'A': 1}
}
start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print(shortest_distances)

"""dynamic implementaion
n=int(input("enter the number of times:"))
for i in range(n):
  key = eval(input("enter key"))
  value = eval(input("enter value"))
  d[key] = value
  
dfs(graph,'a')"""