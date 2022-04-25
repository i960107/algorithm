from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def BSTToGreaterSumTree_Fail(self, root: TreeNode) -> Optional[TreeNode]:
        # 오른쪽 서브트리 값의 합이 아니라 전체 트리에 대해서 다기보다 큰 값
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            answer = node.val
            dfs(node.left)
            answer += dfs(node.right)
            node.val = answer
            return answer

        dfs(root)
        return root
    val: int = 0

    def bstToGst_inorder(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        # 큰 값부터 순회하면서 전체 합 값 쌓기
        # 자신보다 같거나 큰 값을 구하려면 자기 자신을 포함한 우측 노드 노드의 합을 구하면 됨.
        if root:
            # 순서 상관이 있나?
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root
