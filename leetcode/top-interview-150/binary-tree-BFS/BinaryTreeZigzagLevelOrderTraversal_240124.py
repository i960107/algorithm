from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    #  zigzag 의미 파악이 중요!
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        ans = []
        row = 0
        while queue:
            size = len(queue)
            result = []
            for _ in range(size):
                node = queue.popleft()
                if not node:
                    continue
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            # 최대 깊이 10, 한 레벨 당 최대 노드 수 2 ^ 10 -1로 TLE 나지 않지만 매번 뒤집어야하는 것은 비효율적.
            if result:
                ans.append(result if row % 2 == 0 else result[::-1])
            row += 1
        return ans

    def zigzagLevelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        row = 0
        while queue:
            size = len(queue)
            result = [None] * size
            for i in range(size):
                node = queue.popleft()
                if not node:
                    continue
                result[i if row % 2 == 0 else (size - 1) - i] = node.val
                # 주의 leaf노드 다음 레벨도(없는 레벨) 덱에 넣으면 result가 빈 배열이 아니므로 체크 불가능.
                # root가 빈노드일때도 주의.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(result)
            row += 1
        return ans
