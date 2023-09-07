import math
from typing import List, Optional, Iterator
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 트리는 빈 트리일 수 없다.
    #  노드의 값은 음수가 될 수 있다.
    # answes within 10 ^ -5 of the actual answer will be accepted  -> 소수점 다섯째자리까지 비교됨.
    # 반올림안해줘도됨.
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            next_queue = deque()
            total = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                if node.left:
                    next_queue.append(node.left)
                # next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(total / size)
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
print(s.averageOfLevels(makeBST([3, 9, 20, None, None, 15, 7])))
print(s.averageOfLevels(makeBST([3, 9, 20, 15, 7])))
print(s.averageOfLevels(makeBST([3])))
