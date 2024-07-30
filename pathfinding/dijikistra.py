import heapq
def dijkstra(graph, start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    queue = [(0,start)]

    while queue:
        current_distance ,current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for n , w in graph[current_node].items():
            current = current_distance+w
            if current < distances[n]:
                distances[n] = current
                heapq.heappush(queue,(current,n))
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