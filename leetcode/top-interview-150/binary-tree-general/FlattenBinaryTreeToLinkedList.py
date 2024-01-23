from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = None

    def flatten_fail(self, root: Optional[TreeNode]):
        # head and tail 둘다 알아야하는데..
        # in place 해야함. 반환 값 없이 root자체가 변환되어야함.
        ll = TreeNode()

        def _flatten(node):
            if not node:
                return
            print(node.val)
            ll.right = TreeNode(node.val)
            _flatten(node.left)
            _flatten(node.right)

        _flatten(root)
        return ll.right

    # 부모만 알고 있으면 되나?
    def flatten(self, root: Optional[TreeNode]):
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
