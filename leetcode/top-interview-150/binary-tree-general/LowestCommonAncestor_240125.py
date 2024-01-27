from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestorFail(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        p_path = {}
        q_path = {}
        nodes = {}

        def getPath(node):
            if not node or (p_path and q_path):
                return
            path.append(node)
            if node.val == p.val:
                for i, node in enumerate(path):
                    p_path[node.val] = i
            elif node.val == q.val:
                for i, node in enumerate(path):
                    q_path[node.val] = i
                    nodes[i] = node
            getPath(node.left)
            getPath(node.right)
            path.pop()

        getPath(root)

        # lowest common node찾기.
        if len(p_path) > len(q_path):
            p_path, q_path = q_path, p_path

        lowest_index = 10 ** 5 + 1
        for val in p_path:
            if val in q_path and q_path[val] < lowest_index:
                lowest_index = q_path[val]
        # value가 아니라 tree node 자체를 반환해야함.
        return nodes[lowest_index]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None
        ans_level = -1

        def dfs(node: Optional['TreeNode'], level: int) -> List[int]:
            result = [False, False]

            if not node:
                return result

            left_result = dfs(node.left, level + 1)
            result[0] |= left_result[0]
            result[1] |= left_result[1]

            right_result = dfs(node.right, level + 1)
            result[0] |= right_result[0]
            result[1] |= right_result[1]

            if node.val == p.val:
                result[0] = True

            if node.val == q.val:
                result[1] = True

            nonlocal ans, ans_level
            if result[0] and result[1] and ans_level < level:
                ans = node
                ans_level = level
            return result

        dfs(root, 0)
        return ans

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        if root is None:
            return None

        if root == p or root == q:
            return root

        leftNode = self.lowestCommonAncestor2(root.left, p, q)
        rightNode = self.lowestCommonAncestor2(root.right, p, q)

        # 둘 중 하나 이상이 None이라면 None이 반한. 둘다 값이 있다면 rightNode(None None)이 반환.
        # all value if unique. left node and right node인 경우 하나밖에 없음!
        if leftNode and rightNode:
            return root

        return leftNode or rightNode




print(0 and 3)  # 0. and -> return first false value if exist else return last value
print(1 and 3)  # 3
print(0 or 3)  # 3 return first true value if exist else return False
print(1 or 3)  # 1

s = set()
s.add(1)
print(True and s)  # s
print(False and s)  # False
print(None and s)  # None
print(s and True)  # True
print(s and False)  # False
print(s and None)  # None
