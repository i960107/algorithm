class Solution:
    def maxDepth(self, root):
        def _maxDepth(node):
            if not node:
                return 0
            left = _maxDepth(node.left)
            right = _maxDepth(node.right)
            return left + 1 if left >= right else right + 1

        return _maxDepth(root)
