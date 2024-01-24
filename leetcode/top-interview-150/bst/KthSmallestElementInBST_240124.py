class Solution:
    def kthSmallest(self, root, k) -> int:
        rank = 0  # 작은순서대로

        # 전체 다 탐색하지 않고 중간에 멈추고 싶다면?
        def inorder_traversal(node):
            if not node:
                return None

            result = inorder_traversal(node.left)
            if result is not None:
                return result

            nonlocal rank
            rank += 1
            if rank == k:
                return node.val

            result = inorder_traversal(node.right)
            if result is not None:
                return result

            return None

        return inorder_traversal(root)
