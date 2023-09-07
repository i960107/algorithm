from typing import List, Optional, Iterator
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 트리는 빈 트리일 수 있다.
    #  노드의 값은 음수가 될 수 있다.
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if level < len(result):
                result[level] = node.val
            else:
                result.append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return result

    def rightSideView2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            next_queue = deque()
            size = len(queue)
            for n in range(size):
                node = queue.popleft()
                if n == 0:
                    result.append(node.val)
                if node.right:
                    next_queue.append(node.right)
                if node.left:
                    next_queue.append(node.left)
            queue = next_queue
        return result


def makeBST(arr: List[int]) -> Optional[TreeNode]:
    def create(it: Iterator[int]):
        value = next(it)
        return TreeNode(value) if value is not None else None

    if len(arr) == 0:
        return None

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
# print(s.rightSideView(makeBST([1, 2, 3, None, 5, None, 4])))
# print(s.rightSideView(makeBST([1, 2])))
# print(s.rightSideView(makeBST([1, None, 3])))
# print(s.rightSideView(makeBST([])))
# print()
# print(s.rightSideView2(makeBST([1, 2, 3, None, 5, None, 4])))
# print(s.rightSideView2(makeBST([1, 2])))
# print(s.rightSideView2(makeBST([1, None, 3])))
print(s.rightSideView2(makeBST([])))
