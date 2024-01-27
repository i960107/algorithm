from typing import List, Optional


# 1. inorder 를 root 노드를 기준으로 왼쪽, 오른쪽으로 쪼갠다. -> 재귀적인 구조를 생각.
# 2. root 노드를 처음으로 방문하는 방향으로(post order를 거꾸로, preorder)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        def printTree(node: Optional['TreeNode']):
            if not node:
                return ''

            s = printTree(node.left)
            s += (str(node.val) + ' ')
            s += printTree(node.right)
            return s

        return printTree(self)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_pos = {n: i for i, n in enumerate(inorder)}

        def __buildTree(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            root_val = postorder.pop()
            root_pos = inorder_pos[root_val]

            root = TreeNode(root_val)
            root.right = __buildTree(lo, root_pos - 1)
            root.left = __buildTree(root_pos + 1, hi)
            return root

        return __buildTree(0, len(inorder_pos) - 1)


s = Solution()
print("result", s.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]))
print("result", s.buildTree(inorder=[1, 2, 3, 4], postorder=[1, 4, 3, 2]))
