import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))

    def dijkstra(self, start):
        priority_queue = [(0, start)]
        visited = set()
        distances = {node: float('infinity') for node in self.nodes}
        distances[start] = 0

        while priority_queue:
            (current_distance, current_node) = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            for (neighbor, weight) in self.edges[current_node]:
                if neighbor not in visited:
                    new_distance = current_distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(priority_queue, (new_distance, neighbor))

        print(f"Shortest distances from {start}: {distances}")

cities_graph = Graph()

cities_graph.add_node('Tell-aviv')
cities_graph.add_node('ramat-hsharon')
cities_graph.add_node('ramat-gan')
cities_graph.add_node('umm-el-fahem')
cities_graph.add_node('givataytem')
cities_graph.add_node('same') 
cities_graph.add_node('arrar') 

cities_graph.add_edge('Tell-aviv', 'ramat-hsharon', 1)
cities_graph.add_edge('ramat-gan', 'ramat-hsharon', 4)
cities_graph.add_edge('umm-el-fahem', 'Tell-aviv', 3)
cities_graph.add_edge('givataytem', 'ramat-gan', 2)
cities_graph.add_edge('givataytem', 'ramat-hsharon', 2)
cities_graph.add_edge('Tell-aviv', 'ramat-gan', 5)
cities_graph.add_edge('same', 'Tell-aviv', 1)
cities_graph.add_edge('arrar', 'umm-el-fahem', 3)

start_vertex = 'arrar'
cities_graph.dijkstra(start_vertex)
