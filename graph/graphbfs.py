def bfs(graph, start):
  visited = set()
  queue = [start] 

  while queue:
    vertex = queue.pop(0)   
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)


graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

bfs(graph, 'A')
