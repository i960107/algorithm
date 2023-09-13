'''인접 행렬로 구현한 무방향, 비가중 그래프 '''
from typing import List


class Graph:
    def __init__(self, numberOfVertices: int):
        self.numberOfVertices = numberOfVertices
        self.matrix = [[0] * numberOfVertices for _ in range(numberOfVertices)]

    def hasEdge(self, u: int, v: int) -> bool:
        return self.matrix[u][v] == 1

    def addEdge(self, u: int, v: int) -> None:
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def removeEdge(self, u: int, v: int) -> None:
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def getAdjacentVertices(self, u: int) -> List[int]:
        result = []
        for v in range(self.numberOfVertices):
            if self.matrix[u][v] == 1:
                result.append(v)
        return result

    def getDegree(self, u: int) -> int:
        count = []
        for v in range(self.numberOfVertices):
            if self.matrix[u][v] == 1:
                count += 1
        return count

    def __str__(self):
        pass
