class Solution:
    def invertTree(self, root):
        def _invertTree(node):
            if not node:
                return

            node.left, node.right = node.right, node.left
            _invertTree(node.left)
            _invertTree(node.right)

        _invertTree(root)
        return root
