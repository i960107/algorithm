from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 각 레벨의 가장 오른쪽 node
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = deque()
        queue.append((root, 0))
        prev_level = -1
        ans = []
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            if prev_level < level:
                ans.append(node.val)
                prev_level = level
            queue.append((node.right, level + 1))
            queue.append((node.left, level + 1))
        return ans
