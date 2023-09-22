from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def _countNodes(node: Optional[TreeNode]):
            if node is None:
                return None
            left = _countNodes(node.left)
            right = _countNodes(node.right)
            return left + right + 1

        return _countNodes(root)
