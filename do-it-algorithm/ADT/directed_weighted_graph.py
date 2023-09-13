'''인접 리스트로 구현한 무방향, 비가중 그래프 '''
# 자바였다면 LinkedList의 배열을 가짐.
# 혹은 인접 노드의 인덱스 리스트(set)를 가질 수 있음
from typing import List, Set, Any


class Vertex:
    def __init__(self, value: int):
        self.value = value
        self.edges = set()

    def addEdge(self, dest: Any, weight: int):
        self.edges.add(Edge(self, dest, weight))

    def __str__(self):
        return '%d : %s' % (self.value, ', '.join(str(x) for x in self.edges))

    def __lt__(self, other):
        return self.value < other.value


class Edge:
    def __init__(self, src: Vertex, dest: Vertex, weight: int):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __str__(self):
        return '%d(%d)' % (self.dest.value, self.weight)


class Graph:
    def __init__(self, numberOfVertices: int):
        self.numberOfVertices = numberOfVertices
        self.vertices = set()

    def hasEdge(self, u: Vertex, v: Vertex) -> bool:
        return v in u.edges

    def addEdge(self, u: Vertex, v: Vertex, w: int) -> None: u.addEdge(v, w)

    def addVertex(self, value: int) -> Vertex:
        vertex = Vertex(value)
        self.vertices.add(vertex)
        return vertex

    def __str__(self):
        return '\n'.join(str(x) for x in sorted(self.vertices))


graph = Graph(6)
graph0 = graph.addVertex(0)
graph1 = graph.addVertex(1)
graph2 = graph.addVertex(2)
graph3 = graph.addVertex(3)
graph4 = graph.addVertex(4)
graph5 = graph.addVertex(5)

graph.addEdge(graph0, graph1, 9)
graph.addEdge(graph0, graph2, 7)
graph.addEdge(graph0, graph3, 5)
graph.addEdge(graph0, graph5, 6)

graph.addEdge(graph1, graph0, 9)
graph.addEdge(graph1, graph2, 9)

graph.addEdge(graph2, graph0, 9)
graph.addEdge(graph2, graph1, 9)
graph.addEdge(graph2, graph4, 5)

graph.addEdge(graph3, graph0, 5)
graph.addEdge(graph3, graph5, 5)

graph.addEdge(graph4, graph2, 5)
graph.addEdge(graph4, graph5, 1)

graph.addEdge(graph5, graph0, 6)
graph.addEdge(graph5, graph3, 5)
graph.addEdge(graph5, graph4, 1)

print(graph)
