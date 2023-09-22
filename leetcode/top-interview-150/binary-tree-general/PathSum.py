from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # root to leaf
    # 빈 트리일 수 있음
    # 음수 값을 가질 수 있음
    # [1,2] 1은 false 오른쪽 tree는 root to leaf path 없음
    # leaf is a node with no children. root -> children 1 있으므로 leaf아님.
    # tree의 dsf
    # root to leaf
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs
        def _hasPathSum(node: Optional[TreeNode], acc: int):
            acc += node.val
            if node.left is None and node.right is None:
                if targetSum == acc:
                    return True
                return False
            if node.left and _hasPathSum(node.left, acc):
                return True
            if node.right and _hasPathSum(node.right, acc):
                return True
            return False

        return _hasPathSum(root, 0) if root else False
