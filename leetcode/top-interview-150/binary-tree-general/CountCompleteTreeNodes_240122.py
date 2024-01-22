class Solution:
    def countNodes(self, root):
        def _countNodes(node):
            if not node:
                return 0
            return 1 + _countNodes(node.left) + _countNodes(node.right)
        return _countNodes(root)


s = Solution()
print(s.countNodes())
