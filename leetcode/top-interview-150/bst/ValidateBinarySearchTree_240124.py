from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # inorder traversal의 결과가  오름차순인지 살펴보면 안됨?
    # 이렇게 하면 안되는 이유 ->
    def isValidBST_fail(self, root: Optional[TreeNode]) -> bool:
        def _isValidBST(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            res = _isValidBST(node.left)
            if not res:
                return False
            res = _isValidBST(node.right)
            if not res:
                return False
            return (not node.left or node.left.val < node.val) and (not node.right or node.right.val > node.val)

        return _isValidBST(root)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -float('INF')

        # outer scope variable 두는 것 보다 boolean을 return하는게 더 좋은 방법인가?
        # 어차피 둘다 매번 확인해야하므로 똑같을듯.
        # 근데 메모리 왔다갔다 하는 것 보다는 return값 확인하는게 더 좋을수도

        def inorder(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            result = inorder(node.left)
            if result is False:
                return result

            nonlocal prev
            if prev >= node.val:
                return False
            prev = node.val

            result = inorder(node.right)
            if result is False:
                return result

            return True

        return inorder(root)
