from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0
        path = []

        def _sumNumbers(node: Optional[TreeNode]):
            path.append(str(node.val))

            if node.left:
                _sumNumbers(node.left)
            if node.right:
                _sumNumbers(node.right)

            if not node.left and not node.right:
                # leaf 노드인 경우:
                nonlocal sum
                sum += int(''.join(path))
            path.pop()

        _sumNumbers(root)
        return sum
