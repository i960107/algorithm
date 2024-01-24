from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 각 레벨별로 미리 queue의 길이를 기록해두고 -> 새로 삽입된 노드는 다른 레벨의 것.
    # for문으로 해결하는 방법도 있음.
    def averageOfLevels(self, root) -> List[float]:
        level = 0
        total, count = 0, 0
        # 주의 -> root, 1 각각 item으로 들어감.
        # queue = deque((root, 0))
        queue = deque()
        queue.append((root, 0))
        ans = []
        while queue:
            node, node_level = queue.popleft()
            if not node:
                continue
            # if level == node_level:
            #     total += node.val
            #     count += 1
            # else:
            #     ans.append(total / count)
            #     total = node.val
            #     count = 1
            #     level = node_level
            if level < node_level:
                ans.append(total / count)
                level = node_level
                total = 0
                count = 0
            total += node.val
            count += 1
            queue.append((node.left, node_level + 1))
            queue.append((node.right, node_level + 1))

        ans.append(total/count)
        return ans
