from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    # 미리 inorder traversal 결과를 만들어두고 반환한다.
    def __init__(self, root: Optional[TreeNode]):
        self.traversal = self.desc_traversal(root)

    def desc_traversal(self, node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []
        result = self.desc_traversal(node.right)
        result.append(node.val)
        result += self.desc_traversal(node.left)
        return result

    def next(self) -> int:
        return self.traversal.pop()

    def hasNext(self) -> bool:
        return self.traversal
