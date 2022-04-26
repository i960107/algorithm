import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    minimum: int = 0

    def minimum_distance_between_nodes(self, root: TreeNode) -> Optional[int]:
        # 전체 탐색해야 하는 것 아닌가?
        # o(N^2)보다 빠른 알고리즘?
        # 정렬된 결과이기 때문에 distance가 가장 가까운 노드는 자기랑 연결된 노드들 중 있음?
        # 아님!!!!
        # 연결된 노드 간 거리가 아니라 중위 순회한 앞뒤 결과를 봐야해!
        # 루트와 가장 차이가 작을 수 있는 노드는? 왼쪽 서브트리 중 가장 큰 값과 오른쪽 서브트리의 가장 작은 값 중 하나
        if not root:
            return None

        left = self.minimum_distance_between_nodes(root.left)
        left_distance = root.val - root.left.val
        right = self.minimum_distance_between_nodes(root.right)
        right_distance = root.right.val - root.val

        return min(left, left_distance, right, right_distance)

    prev = -sys.maxsize
    result = sys.maxsize

    def minimum_distance_between_nodes_recursive(self, root: TreeNode) -> Optional[int]:
        '''재귀 구조로 중위 순회'''

        # 왼쪽 노드에 대해서 min distance 구하기
        # 가장 왼쪽 노드에 대해서 가장 작은 node 부터 값 비교 시작
        if root.left:
            self.minimum_distance_between_nodes_recursive(root.left)

        # 중간 노드에 대해 연산
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        # 왜 왼쪽 노드에 대해서만 하지? greedy algorithm?
        if root.right:
            self.minimum_distance_between_nodes_recursive(root.right)

        return self.result

    def minimum_distance_between_nodes_iterative(self, root: TreeNode) -> Optional[int]:
        '''반복 구조로 중위 순회'''
        # math.inf 최대 Float값
        # sys.maxsize 최대 int값
        # prev 초기화 값: 가장 작은 원소보다 작으면서, 차이가 최대로 나오록
        # result 초기화 값: prev -sys.maxsize 이면서 curr sys.maxsize인 경우 차이?
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        while stack or node:
            # node 포함 왼쪽 서브트리 탐색
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result
