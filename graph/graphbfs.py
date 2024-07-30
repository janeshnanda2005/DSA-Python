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

"""dynamic implementaion
n=int(input("enter the number of times:"))
for i in range(n):
  key = eval(input("enter key"))
  value = eval(input("enter value"))
  d[key] = value
  
dfs(graph,'a')"""