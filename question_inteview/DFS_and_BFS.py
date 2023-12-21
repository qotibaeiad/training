
from collections import deque as stack

class Graph:
    def __init__(self):
        self.graph={}
    
    def add_neighbor(self,vertex,neighbor):
        if(vertex not in self.graph):
            self.graph[vertex]=[]
        self.graph[vertex].append(neighbor)
    
    def DFS(self,start,visited=None):
        if(visited is None):
            visited=set()
        visited.add(start)
        print(start,end=' ')
        for neighbor in self.graph.get(start,[]):
            if neighbor not in visited:
                self.DFS(neighbor,visited)

    def BFS(self,start):
        visited = set()
        queue = stack([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex,end=' ')
                visited.add(vertex)
                for neighbor in self.graph.get(vertex,[]):
                    if neighbor not in visited:
                        queue.append(neighbor)


g = Graph()

g.add_neighbor("tel-aviv", "ramat-gan")
g.add_neighbor("ramat-gan", "ramat-hasharon")
g.add_neighbor("umm-el-fahem", "ar'ara")
g.add_neighbor("ramat-gan", "umm-el-fahem")
g.add_neighbor("ar'ara","ramat-gan")
g.BFS("umm-el-fahem")




















"""
    def BFS(self,start):
        visited = set()
        queue = stack([start]) # or | queue = stack() 
                               #    | queue.append(astart)
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex,end=' ')
                visited.add(vertex)
                for neighbor in self.graph.get(vertex,[]):
                    if neighbor not in visited:
                        queue.append(neighbor)
"""
























































"""
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self,vertex,neighbor):
        if(vertex not in self.graph):
            self.graph[vertex]=[]
        self.graph[vertex].append(neighbor)

    def DFS(self,start,visited=None):
        if(visited is None):
            visited = set()
        visited.add(start)
        print(start,end=' ')
        for neighbor in self.graph.get(start,[]):
            if(neighbor not in visited):
                self.DFS(neighbor,visited)



g = Graph()
g.add_edge(1, 2)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 1)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth-First Traversal (DFS):")
g.DFS(0)
"""