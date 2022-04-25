from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total: int = 0

    def range_sum_of_bst(self, root: TreeNode, L: int, R: int) -> int:
        if root:

            if root.val < R:
                self.range_sum_of_bst(root.right)

            if root.val <= R and root.val >= L:
                self.total += root.val

            if root.val < L:  # root.val <= R
                return self.total
            else:
                self.range_sum_of_bst(root.left)

        return root

    def rangeSumBST1(self, root: TreeNode, L: int, R: int) -> int:
        '''재귀 구조 DFS로 브루트 포스 검색'''
        # DFS로 전체를 탐색한 다음 L과 R사이일때만 값 더하기

        if not root:
            return 0
        return (root.val if L <= root.val <= R else 0) + \
               self.rangeSumBST1(root.left, L, R) + \
               self.rangeSumBST1(root.right, L, R)

    total2: int = 0

    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:
        '''DFS 가지치기로 필요한 노드 검색'''
        # 두 가지 중 필요한 서브트리만 탐색
        if not root:
            return 0

        if L <= root.val <= R:
            self.total2 += root.val
            self.rangeSumBST1(root.left, L, R)
            self.rangeSumBST1(root.right, L, R)

        elif root.val < L:
            self.rangeSumBST1(root.right, L, R)
        else:
            self.rangeSumBST1(root.left, L, R)

        return self.total2

    def rangeSumBST3(self, root: TreeNode, L: int, R: int) -> int:
        '''반복 구조 DFS로 필요한 노드 탐색'''
        # 스택에 쌓기!!!
        stack = [root]
        total = 0

        while stack:
            node = stack.pop()
            # leaf node의 자식의 경우 None임
            if node:
                #  node.val == L 혹은 node.val == R인 경우 자식은 탐색하지 않음
                # L < node.val < R 인 경우
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    total += node.val
            # 등호 관계 주의
            # node.val == L일때 node.left, node.right 탐색하는 것 불필요!
            # if L <= node.val <= R:
            #     total += node.val
            #     stack.append(node.left)
            #     stack.append(node.right)
            # elif node.val < L:
            #     stack.append(node.right)
            # else:
            #     stack.append(node.left)

        return total

    def rangeSumBST4(self, root: TreeNode, L: int, R: int) -> int:
        '''반복 구조 BFS로 필요한 노드 검색'''
        stack = deque([root])
        total = 0
        while stack:
            node = stack.popleft()
            if node:
                if L <= node.val <= R:
                    total += node.val

                # node의 값에 따라서 왼쪽 오른쪽 서브트리 선택
                # 너비 우선 탐색이라고 그 레벨의 모든 노드를 반드시 탐색해야 하는 것 아님

                # 어떻게 다르지?
                # if node.val < L:
                #     stack.append(node.right)
                # if node.val > R:
                #     stack.append(node.left)

                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return total
