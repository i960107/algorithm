from typing import List, Optional
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def solution_bfs(root: TreeNode) -> Optional[TreeNode]:
        '''반복구조로 BFS'''
        if not root:
            return None

        stack = deque([root])

        # 부모 노드부터 하향식 스왑
        while stack:
            node = stack.popleft()
            # 위에서부터 swap하면 그 노드를 루트로한 서브트리 전체가 swap되는 효과
            if node:
                node.left, node.right = node.right, node.left
                # 너비우선이기때문에 같은 level의 노드 사이에 차이 없음
                stack.append(node.left)
                stack.append(node.right)
        return root

    def solution_pythonic(self, root: TreeNode) -> TreeNode:
        '''pythonic한 방법'''
        # 재귀 풀이: 리프노드까지 내려가서 백트래킹하면서 스왑하는 상향 방식
        if root:
            root.left, root.right = \
                self.solution_pythonic(root.right), self.solution_pythonic(root.left)
            return root

        return None

    def solution_dfs(self, root: TreeNode) -> TreeNode:
        stack = deque([root])

        # 부모 노드부터 하향식 스왑
        # 전위순회형태 ?
        while stack:
            # dfs는 pop()으로추출
            node = stack.pop()
            node.left, node.right = node.right, node.left
            # 바뀐 결과를 추가
            # 삽입하는 순서 바뀌면 결과도 달라지나?
            stack.append(node.left)
            stack.append(node.right)

        return root

    def solution_dfs_postorder(self, root: TreeNode) -> TreeNode:
        stack = deque([root])
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                # 후위 순회??왜?
                node.left, node.right = node.right, node.left

        return root