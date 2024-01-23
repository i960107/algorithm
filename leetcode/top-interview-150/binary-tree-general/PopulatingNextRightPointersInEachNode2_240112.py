from collections import deque


class Node:
    def __init__(self, val=0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # bfs 아닌가.
    def connect(self, root: 'Node') -> 'Node':
        prev = root
        prev_level = 0
        queue = deque()
        queue.append((root.left, 1))
        queue.append((root.right, 1))
        # level을 기록해야하나..
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            if prev_level == level:
                prev.next = node
            prev, prev_level = node, level
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        return root
