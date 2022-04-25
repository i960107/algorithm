import math
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
        # 정렬된 결과이기 때문에 distance가 가장 가까운 노드는 자기랑 연결된 노드들 중 있음
        if not root:
            return None

        left = self.minimum_distance_between_nodes(root.left)
        left_distance = root.val - root.left.val
        right = self.minimum_distance_between_nodes(root.right)
        right_distance = root.right.val - root.val

        return min(left, left_distance, right, right_distance)

    def minimum_distance_between_nodes_recursive(self, root: TreeNode) -> Optional[int]:
        '''재귀 구조로 중위 순회'''
        pass

    def minimum_distance_between_nodes_iterative(self, root: TreeNode) -> Optional[int]:
        '''반복 구조로 중위 순회'''
        # math.inf 최대 Float값
        # sys.maxsize 최대 int값
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root
        while stack or node:
            while node
            node = stack.pop()
            stack.append(node.left)
            stack.append(node.right)
