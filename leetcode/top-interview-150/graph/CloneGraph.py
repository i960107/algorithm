from typing import List, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# 그래프를 deepcopy한 새로운 그래프를 만드는 문제. 노드들을 새로운 객체로 생성해야함.
# 빈 그래프일 수 있다.
# node.val = node의 인덱스(1부터 시작)이며 유일한 값이다.
# 루프 간선이나, 중복된 간선은 없다.
# 연결 그래프이다(임의의 노드 x에서 dfs시 모든 노드 방문)
# 무방향 그래프이다.
# 항상 첫번째 노드가 매개변수로 주어짐.
# 전체 노드를 탐색해야한다 -> bfs, dfs 둘다 상관 없음.
# 같은 객체를 사용해야한다 -> 딕셔너리 필요
# python에서 type hint class name string 혹은 클래스 둘다 쓸 수 있는데.
# Forward Declarations: Node 클래스가 코드 뒷부분에 선언되어 있을때, Node 클래스가 다른 모듈에 선언되어있을때, 
class Solution:

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        new_nodes = dict()
        stack = []
        visited = set()

        stack.append(node)
        visited.add(node)
        new_nodes[node.val] = Node(node.val)

        # visited를 전에 체크하고 빼서 visited체크하면 안됨. 같은 곳에서 체크해야함.
        # 처음 stack 넣을때도!

        while stack:
            curr = stack.pop()
            new_node = new_nodes[curr.val]
            for adj in curr.neighbors:
                nxt_node = new_nodes[adj.val] if adj.val in new_nodes else Node(adj.val)
                new_node.neighbors.append(nxt_node)
                new_nodes[adj.val] = nxt_node
                if adj in visited:
                    continue
                stack.append(adj)
                visited.add(adj)
        return new_nodes[1]


def makeGraph(adjList: List[List[int]]) -> Optional[Node]:
    d = dict((i, Node(i, None)) for i in range(1, len(adjList) + 1))
    for i, adjs in enumerate(adjList, 1):
        for nxt in adjs:
            d[i].neighbors.append(d[nxt])

    for i in range(1, len(adjList)):
        print(i, end=' : ')
        for nxt in d[i].neighbors:
            print(nxt.val, end=' ')
        print()
    return d[1]


def getGraph(node: Optional['Node']):
    visited = set()
    stack = []
    stack.append(node)
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        print(node.val, [x.val for x in node.neighbors])
        visited.add(node)
        for nxt in node.neighbors:
            stack.append(nxt)


s = Solution()
print(getGraph(s.cloneGraph(makeGraph([[2, 4], [1, 3], [2, 4], [1, 3]]))))
