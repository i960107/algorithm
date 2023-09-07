import sys
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # root노드가 없거나 root노드만 존재하는 경우는 없다.
    # getMin, getMax를 하는게 중복된 작업 아닌가? 줄일 수 없나?
    # min_diff는 최소 1 이상. 1인 값을 한번이라도 찾았으면 더 작은 값 나올 수 없으므로 함수 종료 -> 불필요한 작업 줄일 수 있음.

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = 10 ** 5 + 1

        def __getMinimumDiffernce(root: Optional[TreeNode]):
            nonlocal min_diff
            if min_diff == 1:
                return
            if root.left:
                maxInLeft = self.getMax(root.left)
                if root.val - maxInLeft < min_diff:
                    min_diff = root.val - maxInLeft
                __getMinimumDiffernce(root.left)

            if root.right:
                minInRight = self.getMin(root.right)
                if minInRight - root.val < min_diff:
                    min_diff = minInRight - root.val
                __getMinimumDiffernce(root.right)

        __getMinimumDiffernce(root)
        return min_diff

    # def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
    #     min_diff = 10 ** 5 + 1
    #
    #     def __getMinimumDiffernce(node: Optional[TreeNode]):
    #         nonlocal min_diff
    #
    #         if min_diff == 1:
    #             return
    #
    #         temp = node.val
    #         if node.left:
    #             __getMinimumDiffernce(node.left)
    #             if node.val - node.left.val < min_diff:
    #                 min_diff = node.val - node.left.val
    #             if abs(root.val - temp) > abs(root.val - node.left.val):
    #                 temp = node.left.val
    #         if node.right:
    #             __getMinimumDiffernce(node.right)
    #             if node.right.val - node.val < min_diff:
    #                 min_diff = node.right.val - node.val
    #             if abs(root.val - temp) > abs(root.val - node.right.val):
    #                 temp = node.right.val
    #         print(node.val, node.left.val if node.left is not None else None, node.right.val if node.right is not None else None, min_diff)
    #         node.val = temp
    #
    #     __getMinimumDiffernce(root)
    #     return min_diff

    # BST를 재귀함수를 사용해서 깊이우선탐색(DFS)하는 것은 쉬움.
    # BST를 stack을 사용해서 깊이 우선 탐색(DFS)하는 것은 어려움
    # def dfs(self, root: Optional[TreeNode]):
    #     stack = []
    #     node = root
    #     while (stack or node):
    #         while node:
    #             stack.append(node)
    #             node = node.left
    #
    #         node = stack.pop()
    #         print(node.val)
    #
    #         node = node.right
    # 중위순회한 결과는 오름차순. 한쪽방향으로 검색하면 모든 노드에 대해 검새가능.
    # a.right - a = 사실은 a.right.right - a.right이기 때문.

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        stack = []
        node = root

        while (stack or node) and result != 1:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right
        return result

    def getMax(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        curr = root
        while curr.right is not None:
            curr = curr.right
        return curr.val

    def getMin(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr.val


def makeBST(arr: List[int]) -> Optional[TreeNode]:
    # def __makeBST(index: int):
    #     # 주의 자식이 없지만 인덱스가 작을 수 있음
    #     if index >= len(arr) or arr[index] is None:
    #         return None
    #     left = __makeBST(index * 2 + 1)
    #     right = __makeBST(index * 2 + 2)
    #     return TreeNode(arr[index], left, right)
    #
    # return __makeBST(0)
    root = TreeNode(arr[0])
    stack = [root]
    index = 1
    while stack:
        parent = stack.pop()
        left = None
        if index < len(arr) and arr[index] is not None:
            left = TreeNode(arr[index])
        index += 1

        right = None
        if index < len(arr) and arr[index] is not None:
            right = TreeNode(arr[index])
        index += 1

        parent.left = left
        parent.right = right

        if parent.right is not None:
            stack.append(parent.right)
        if parent.left is not None:
            stack.append(parent.left)
    return root


s = Solution()
# print(s.getMinimumDifference(makeBST([4, 2, 6, 1, 3])))
# print(s.getMinimumDifference2(makeBST([4, 2, 6, 1, 3])))
# print()
# print(s.getMinimumDifference(makeBST([1, 0, 48, None, None, 12, 49])))
# print(s.getMinimumDifference2(makeBST([1, 0, 48, None, None, 12, 49])))
# print()
# 주의!
# print(s.getMinimumDifference2(makeBST([1476, 1054, None, 1, None, None, 215, None, 745])))
# print(s.getMinimumDifference(makeBST([1476, 1054, None, 1, None, None, 215, None, 745])))
print(s.dfs(makeBST([1476, 1054, None, 1, None, None, 215, None, 745])))
