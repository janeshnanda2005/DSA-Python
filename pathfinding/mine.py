import heapq

def diki(graph,start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    queue = [(0,start)]
    while queue:
        current_dis,current_node = heapq.heappop(queue)
        if current_dis > distances[current_node]:
            continue
        for n , w in graph[current_node].items():
            dis = current_dis+w
            if dis < distances[n]:
                distances[n] = dis
                heapq.heappush(queue,(dis,n))
    return distances

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2},
    'C': {'B': 1, 'D': 6},
    'D': {'A': 1}
}
start_node = 'A'
shortest_distances = diki(graph, start_node)
print(shortest_distances)
