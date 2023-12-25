import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u]=[]
        self.graph[u].append((v, w, 0))

    def bellman_ford(self, src):
        distance = [float("inf")] * self.V
        distance[self.graph[src][2]] = 0

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


g = Graph(7)
g.add_edge('Tell-aviv', 'ramat-hsharon', 1)
g.add_edge('ramat-gan', 'ramat-hsharon', 4)
g.add_edge('umm-el-fahem', 'Tell-aviv', 3)
g.add_edge('givataytem', 'ramat-gan', 2)
g.add_edge('givataytem', 'ramat-hsharon', 2)
g.add_edge('Tell-aviv', 'ramat-gan', 5)
g.add_edge('same', 'Tell-aviv', 1)
g.add_edge('arrar', 'umm-el-fahem', 3)

start_vertex = 'arrar'
#g.bellman_ford(start_vertex)
g.dijkstra(start_vertex)