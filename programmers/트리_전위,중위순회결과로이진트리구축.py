from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # self를 인자로 받는 함수는 객체를 통해 접근 가능 함
    # self를 인자로 받지 않는 함수는 static함수처럼 클래스명. 함수명으로 접근 가능함
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 전위, 중위, 후위 순회 중 2가지만 있어도 이진 트리를 복원 가능
        # sub-tree 없는 경우 null로 표현되지 않음. 단지 생략된 배열.

        # preorder, inorder 남은 원소 개수 같음?
        # 다름
        # preorder 빈 배열인 경우 없나? preorder가 빈경우 inorder도 빈 배열이므로 참조할 일 없음
        # 범위가 빈 경우 return None
        # 전위 순회 결과는 중위 순회 분할 인덱스
        if inorder:
            index = inorder.index(preorder.pop(0))

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.build_tree(preorder, inorder[0:index])
            node.right = self.build_tree(preorder, inorder[index + 1:])
            return node


s = Solution()
print(s.build_tree_practice(inorder=[9, 3, 15, 20, 7], preorder=[3, 9, 20, 15, 7]))
print(s.build_tree_practice([], []))
