class TreeNode:
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(val='F',
                left=TreeNode('B', TreeNode('A'), TreeNode('D', TreeNode('C'), TreeNode('E'))),
                right=TreeNode('G', None, TreeNode('I', TreeNode('H')))
                )

pre_traversal = []


def preorder_traverse_recursive(root: TreeNode):
    if not root:
        return
    pre_traversal.append(root.val)
    preorder_traverse_recursive(root.left)
    preorder_traverse_recursive(root.right)
    return pre_traversal


def preorder_traverse_iterative(root: TreeNode):
    if not root:
        return []
    traversal = []
    stack = [root]
    while stack:
        curr = stack.pop()
        traversal.append(curr.val)

        # node 가 None일 경우 Stack에 넣으면 stack은 truthy임. 빈 배열만 Falsy
        # right를 먼저 넣어줘야 left가 배열 마지막에 삽입되어서 left먼저 스택에서 꺼내어
        if curr.right:
            stack.append(curr.right)

        if curr.left:
            stack.append(curr.left)
    return traversal


print(preorder_traverse_recursive(root))
print(preorder_traverse_iterative(root))

in_traversal = []


def inorder_traverse_recursive(root: TreeNode):
    if not root:
        return
    inorder_traverse_recursive(root.left)
    in_traversal.append(root.val)
    inorder_traverse_recursive(root.right)
    return in_traversal


def inorder_traverse_iterative(root: TreeNode):
    pass


post_traversal = []


def postorder_traverse_recursive(root: TreeNode):
    if not root:
        return
    postorder_traverse_recursive(root.left)
    postorder_traverse_recursive(root.right)
    pre_traversal.append(root.val)
    return pre_traversal


def postorder_traverse_iterative(root: TreeNode):
    pass
