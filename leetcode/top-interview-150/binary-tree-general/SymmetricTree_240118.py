class Solution:
    def isSymmetric(self, root):
        def _isSymmetric(node1, node2):
            if not (node1 and node2):
                return not node1 and not node2
            if node1.val != node2.val:
                return False
            return _isSymmetric(node1.left, node2.right) & _isSymmetric(node1.right , node2.left)
        return _isSymmetric(root.left, root.right)
