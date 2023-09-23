class Solution:
    def isSymmetric(self, root):
        def _isSymetric(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            if not _isSymetric(left.left, right.right):
                return False
            if not _isSymetric(left.right, right.left):
                return False
            return True


        return _isSymetric(root.left, root.right)
