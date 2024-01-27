from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def __init__(self):
    # self.max_sum = -float('INF')

    # 카데인 알고리즘 응용인데...
    # inner function 없이 구현 가능. return값이 current_sum일때 마지막에는 max_sum이어야함.
    # a node can apear in the sequence at most once -> 왼쪽 혹은 오른쪽 subtree 선택해야함.
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 전체 path 중 최댓값.
        max_sum = -float('INF')

        # 무조건 node를 포함한 path의 최대값.
        # 자기자신만, 한족 서브트리만, 두 서브트리 다 포함하는 path일 수 있음.
        def _maxPathSum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = _maxPathSum(node.left)
            right = _maxPathSum(node.right)

            nonlocal max_sum
            # 위의 노드들에서는 한쪽 path만 선택해야하지만, 현재까지는 왼쪽 오른쪽 다 포함한 path가능.
            if left + right + node.val > max_sum:
                max_sum = left + right + node.val

            current_sum = max(left, right) + node.val
            if current_sum < 0:
                return 0
            else:
                return current_sum

        _maxPathSum(root)
        return max_sum
