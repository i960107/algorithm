from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_pos = {n: i for i, n in enumerate(inorder)}
        pos = 0

        def _buildTree(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            nonlocal pos

            root_val = preorder[pos]
            root_pos = inorder_pos[root_val]
            root = TreeNode(root_val)

            pos += 1

            root.left = _buildTree(lo, root_pos - 1)
            root.right = _buildTree(root_pos + 1, hi)
            return root

        return _buildTree(0, len(preorder) - 1)


s = Solution()
print(s.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
