from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(tree: List[int]) -> int:
    '''인덱스로 탐색'''
    if not tree:
        return 0
    index = 1
    depth = 1
    while index * 2 - 1 < len(tree):
        index *= 2
        depth += 1
    return depth


# Optional: type hint의 일종. None이 허용되는 함수의 매개변수에 대한 타입을 명시.
# Optional[int] -> int or None

def solution_bfs(root: Optional[TreeNode]) -> int:
    '''bfs로 탐색'''
    if not root:
        return 0

    Q = deque([root])
    depth = 0

    while Q:
        depth += 1
        # q에 들어있는 애들은 동일한 level의 노드
        for _ in range(len(Q)):
            # 자식 노드가 부모 노드와 섞이진 않을까?
            # len(Q)만큼 반복하기 때문에 새로 삽입된 자식 노드는 추출되지 않음
            curr_root = Q.popleft()
            if curr_root.left:
                Q.append(curr_root.left)
            if curr_root.right:
                Q.append(curr_root.right)

    return depth


print(solution_bfs(None))
print(solution_bfs(TreeNode(3)))
