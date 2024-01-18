class Solution:
    def isSameTree(self, p, q):
        def _isSameTree(node1, node2):
            if not (node1 and node2):
                return not node1 and not node2

            if node1.val != node2.val:
                return False

            return _isSameTree(node1.left, node2.left) & _isSameTree(node1.right, node2.right)

        return _isSameTree(p, q)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
