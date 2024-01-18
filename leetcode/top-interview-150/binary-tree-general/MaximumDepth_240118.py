from typing import List


class Solution:
    def maxDepth(self, root):
        def _maxDepth(node):
            if not node:
                return 0
            return max(node.left, node.right) + 1

        return _maxDepth(root)


