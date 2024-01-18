class Solution:
    def invertTree(self, root):
        # 순서 상관 없음
        # 바꾸고 다음 레벨로 내려가나, 다음 레벨 다 바꾸고 나서 왼쪽 오른쪽 바꾸나.
        def _invertTree(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            _invertTree(node.left)
            _invertTree(node.right)

        _invertTree(root)
        return root
