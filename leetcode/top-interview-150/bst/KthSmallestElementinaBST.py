import sys
from typing import List, Optional, Iterator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Follow up: If the BST is modified often (i.e., we can do insert and delete operations)
# and you need to find the kth smallest frequently, how would you optimize?

class Solution:
    # 빈트리는 없다.
    # 트리 노드의 값은 0보다 크거나 같다.
    def kthSmallest(self, root: TreeNode, k: int):
        stack = []
        node = root
        count = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            count += 1
            node = stack.pop()
            if count == k:
                return node.val

            node = node.right

    def kthSmallest_recursive(self, root: TreeNode, k: int):
        count = 0
        result = None

        def __kthSmallest(node: TreeNode):
            nonlocal count, k, result

            if node.left:
                __kthSmallest(node.left)

            count += 1
            if count == k:
                result = node.val

            if count < k and node.right:
                __kthSmallest(node.right)

        __kthSmallest(root)
        return result

    def dfs(self, root: Optional[TreeNode]):
        stack = []
        node = root
        while (stack or node):
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            print(node.val)

            node = node.right


def makeBST(arr: List[int]) -> Optional[TreeNode]:
    def create(it: Iterator[int]):
        value = next(it)
        return TreeNode(value) if value is not None else None

    it = iter(arr)
    root = TreeNode(next(it))
    nextLevel = [root]

    try:
        while nextLevel:
            level = nextLevel
            nextLevel = []
            for node in level:
                if not node:
                    continue
                node.left = create(it)
                node.right = create(it)
                nextLevel += [node.left, node.right]
    except StopIteration:
        return root


s = Solution()
# print(s.dfs(makeBST([3, 1, 4, None, 2])))
# print(s.kthSmallest(makeBST([3, 1, 4, None, 2]), 1))
# print()
# print(s.dfs(makeBST([5, 3, 6, 2, 4, None, None, 1])))
# print(s.kthSmallest(makeBST([5, 3, 6, 2, 4, None, None, 1]), 3))
print(s.kthSmallest_recursive(makeBST([5, 3, 6, 2, 4, None, None, 1]), 3))
# print(s.kthSmallest(makeBST([5, 3, 6, 2, 4, None, None, 1]), 6))
