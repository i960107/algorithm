from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution_fail(root: TreeNode) -> int:
    # longest path 왼쪽 서브트리의 level + 오른쪽 서브트리의 level?
    # 한쪽이 많이 깊을경우 그 서브트리의 두 노드를 선택하는게 더 긴 경로일 수 있음
    if not root:
        return 0
    answer = 0

    def get_depth(root: TreeNode) -> int:
        depth = 0
        Q = deque([root])
        while Q:
            depth += 1
            for _ in range(len(Q)):
                curr = Q.popleft()
                if curr.left: Q.append(curr.left)
                if curr.right: Q.append(curr.right)
        return depth

    answer += get_depth(root.left) + 1 if root.left else 0
    answer += get_depth(root.right) + 1 if root.right else 0
    return answer


class Solution:
    longest: int = 0

    def solution(self, root: TreeNode) -> int:
        # 리프노드까지 탐색한 다음 부모로 거슬러 올라가면서 각각의 거리를 계산해 상태값을 업데이트 하면서 누적
        # 중첩 함수에서 부모 함수의 변수를 재할당하게 되면 참조 id가 변경되어 별도의 로컬 변수로 선언됨
        # 부모함수의 변수를 그대로 사용할 수 없고 함수 바깥에서 클래스 변수로 선언후 사용해야 함.
        # 숫자나 문자인 경우 불변 객체이기 때문에 중첩 함수 내에서는 값을 변경할 수 없다.

        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            # 재귀 호출을 통해 왼쪽, 오른쪽의 각 리프노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # longest left, right각각에서 가장 긴 루트
            # 현재 노드로 이어진 서브트리에서 양쪽 노드를 사용해서 가장 긴 루트
            # left + right + 2? 만약 left나 right가 없으면 return -1이기때문에 edge 효과 사라짐
            # 상태값: 리프 노드에서 현재 노드까지의 거리의 최대값
            # 최종 결과가 될 가장 긴 경로
            # 3가지를 비교
            # 1)left 노드에서 가장 긴 path: left
            # 2)right노드에서 가장 긴 path :right
            # 3) left가장 깊은 원소 right의 가장 깊은 원소간 path : left + right + 2
            # 전체 재귀호출에서 공유해야하는 값
            # left, right에 대한 재귀호출 끝난 상태로  각 서브트리에서 가장 긴 path로 값 update된 후
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest

    longest: int = 0

    def solution_test(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)

            return max(left, right) + 1

        dfs(root)

        return self.longest
