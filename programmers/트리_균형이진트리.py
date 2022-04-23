from typing import List, Optional
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode) -> bool:
    # 높이 균형: 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것.
    # 균형이 맞아야 효율적으로 트리를 구성할 수 있으며, 탐색 또한 훨씬 더 효율적임
    # 자가 균형 이진 탐색 트리의 대표: AVL트리 매번 높이 균형을 맞추는

    # 재귀 호출로 leaf노드까지 내려간 후, 깊이 누적해서 올라옴. 차이 1보다 클시 return false
    def check(node: TreeNode):
        if not node:
            return 0
        left = check(root.left)
        right = check(root.right)
        # 양쪽 자식 중 어느 하나가 -1이 되는 경우에는 계속해서 -1을 리턴
        # (한번 -1이 되면 더 이상 회복이 되지 않음)
        # 양쪽 노드 둘다 -1인 경우? return -1
        if left == -1 or \
                right == -1 or \
                abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    return check(root) != -1
