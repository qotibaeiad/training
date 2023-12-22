import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def bellman_ford(self, src):
        distance = [float("inf")] * self.V
        distance[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph_edges():
                if distance[u] != float("inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        for u, v, w in self.graph_edges():
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                print("Graph contains negative-weight cycle")
                return

        print("Bellman-Ford Algorithm:")
        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{distance[i]}")

    def dijkstra(self, src):
        priority_queue = [(0, src)]
        distance = [float("inf")] * self.V
        distance[src] = 0

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distance[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                new_distance = current_distance + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        print("\nDijkstra's Algorithm:")
        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{distance[i]}")

    def graph_edges(self):
        edges = []
        for u in self.graph:
            for v, w in self.graph[u]:
                edges.append((u, v, w))
        return edges


g = Graph(5)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, 3)

start_vertex = 0
g.bellman_ford(start_vertex)

g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, 2)

g.dijkstra(start_vertex)
