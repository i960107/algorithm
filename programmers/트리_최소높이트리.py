from typing import List
from collections import defaultdict


def solution(n: int, edges: List[List[int]]):
    '''단계뼐 리프 노드 제거'''
    # 최소 높이를 구사혈면 가장 가운데 있는 값이 루트여야한다.
    # 리프 노드를 하나씩 제거해 나가면서 남아있는 값을 찾으면 이 값이 가장 가운데 있는 값
    if n <= 1:
        return [0]

    # 양방향 그래프 구성
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    # 첫번째 리프노드 추가
    leaves = []
    for i in range(n + 1):
        if len(graph[i]) == 1:
            leaves.append(i)

    # 루트 노드만 남을때까지 반복 제거
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves

    return leaves
