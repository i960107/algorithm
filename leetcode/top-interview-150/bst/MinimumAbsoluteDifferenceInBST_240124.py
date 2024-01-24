from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 가장 큰 값, 가장 작은 값.
    def getMaximumDifference(self, root: Optional[TreeNode]) -> int:
        curr = root
        while curr:
            curr = curr.right
        max_val = curr.val

        curr = root
        while curr:
            curr = curr.left
        min_val = curr.val

        return max_val - min_val

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 모든 노드에 대해 한번만 방문한다. -> O(N)
        # O(N^2)이 아닌 이유 -> 자기 와 가장 가까운 노드는 자기와 연결된 노드중 하나임.
        # 한쪽 방향으로만 검사할 수 있으면 더 좋은데. -> 일단 최대한 빨리 성공시키고 그 다음에 최적화하는 습관!
        INF = 10 ** 5 + 1
        min_diff = INF
        prev = None

        # 자신을 돌려줌.
        def _getMinimumDifference(node):
            if not node:
                return
            # 실패힝.
            _getMinimumDifference(node.left)
            nonlocal min_diff, prev
            # 주의해야함 prev is not None. prev가 0이 될 수도 있는지 확인하기!!
            if prev and node.val - prev < min_diff:
                min_diff = node.val - prev
            prev = node.val
            _getMinimumDifference(node.right)

        _getMinimumDifference(root)
        return min_diff
