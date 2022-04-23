from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def solution_fail(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 노드값:가장긴path
        max_path = defaultdict(int)

        def dfs(node) -> int:
            if not node:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최대값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.result

    result: int = 0

    def solution(self, root: TreeNode) -> int:
        # 상태 값 return
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # if 문안에서 재귀호출? 값이 달라도 leaf노드까지 재귀호출 해야함
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            # 매 원소 값마다 가장 긴 원소 저장할 필요 없음
            # 매번 가장 긴 경로만 택하면 됨
            self.result = max(self.result, left + right)

            # 자식 노드 상태값 중 큰 값 리턴, 만약 자식 노드 2개 값이 같다면
            # 왼쪽 오른쪽 값이 같아도 한쪽 노드만 선택해야 경로 연장 가능
            # 거리를 차곡차곡 쌓아올라가며 백트래킹하는 형태
            return max(right, left)

        dfs(root)
        return self.result
