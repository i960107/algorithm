'''인접 리스트로 구현한 무방향, 비가중 그래프 '''
# 자바였다면 LinkedList의 배열을 가짐.
# 혹은 인접 노드의 인덱스 리스트(set)를 가질 수 있음
from typing import List, Set


class Graph:
    def __init__(self, numberOfVertices: int):
        self.numberOfVertices = numberOfVertices
        self.graph = dict()
        for v in range(numberOfVertices):
            self.graph[v] = set()

    def hasEdge(self, u: int, v: int) -> bool:
        return v in self.graph[u]

    def addEdge(self, u: int, v: int) -> None:
        self.graph[u].add(v)
        self.graph[v].add(u)

    def removeEdge(self, u: int, v: int) -> None:
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def getAdjacentVertices(self, u: int) -> Set[int]:
        return self.graph[u]

    def getDegree(self, u: int) -> int:
        return len(self.graph[u])

    def __str__(self):
        result = []
        for v, adj in self.graph.items():
            result.append("%d : %s" % (v, adj.__str__()))
        return '\n'.join(result)


graph = Graph(6)
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(0, 3)
graph.addEdge(0, 5)
graph.addEdge(1, 0)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 1)
graph.addEdge(2, 4)
graph.addEdge(3, 0)
graph.addEdge(3, 5)
graph.addEdge(4, 2)
graph.addEdge(4, 5)
graph.addEdge(5, 0)
graph.addEdge(5, 3)
graph.addEdge(5, 4)

print("degree of vertext 0 :", graph.getDegree(0))
print("0 -> 4 is adjacent", graph.hasEdge(0, 4))
print("2 -> 4 is adjacent", graph.hasEdge(2, 4))
print(graph)
