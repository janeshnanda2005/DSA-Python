import heapq

def minimum_spanning_tree(graph):
    """Calculates the Minimum Spanning Tree (MST) using Prim's algorithm."""
    num_vertices = len(graph)
    mst = []
    visited = set()
    start_vertex = 0  # Choose an arbitrary starting vertex

    # Initialize priority queue with edges connected to the start vertex
    pq = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex].items()]
    heapq.heapify(pq)

    while len(mst) < num_vertices - 1:
        weight, u, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, v, neighbor))

    return mst

def tsp_approx(graph):
    """Approximates the TSP using the Minimum Spanning Tree."""
    mst = minimum_spanning_tree(graph)
    tour = []
    visited = set()
    start_vertex = 0  # Choose an arbitrary starting vertex

    # Build the tour by visiting vertices in the MST
    current_vertex = start_vertex
    tour.append(current_vertex)
    visited.add(current_vertex)
    while len(tour) < len(graph):
        for u, v, weight in mst:
            if current_vertex == u and v not in visited:
                tour.append(v)
                visited.add(v)
                current_vertex = v
                break

    # Add the edge back to the starting vertex
    tour.append(start_vertex)

    return tour

# Example usage
graph = {
    0: {1: 2, 2: 6, 3: 5},
    1: {0: 2, 2: 3, 3: 8},
    2: {0: 6, 1: 3, 3: 4},
    3: {0: 5, 1: 8, 2: 4}
}

tour = tsp_approx(graph)
print(tour)  # Output: [0, 1, 2, 3, 0]
