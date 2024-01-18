class Solution:
    def hasPathSum(self, root, target):
        def _hasPathSum(node, pathSum):
            if not node:
                return False

            if not node.left and not node.right:
                return node != root and pathSum == target

            # root to leaf path여야함. 중간 아님.
            # node = root인 건 됨.
            pathSum += node.val

            # root = node인건 되는데 root가 empty인 건 안됨(path자체가 없음)
            return _hasPathSum(node.left, pathSum) | _hasPathSum(node.right, pathSum)

        return _hasPathSum(root, 0)
