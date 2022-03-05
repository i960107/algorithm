from typing import Any
#import 그대로 복사해오는 것이기 때문에 import한 파일도 실행되는 것과 같음.
import h_linked_list_queue as queue


class Node:
    def __init__(self, item: Any):
        # 인덱스 역할을 하는 key필요 없음. getAt()없고 traverse()뿐
        self.item = item
        self.left = None
        self.right = None

    def size(self) -> int:
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self) -> int:
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1

    def preorder_traverse(self) -> list:
        l = []
        l.append(self.item)
        if self.left:
            # list + list: +=, append()둘다 됨
            l += (self.left.preorder_traverse())
        if self.right:
            l += (self.right.preorder_traverse())
        return l

    def inorder_traverse(self) -> list:
        l = []
        if self.left:
            l += (self.left.inorder_traverse())
        l.append(self.item)
        if self.right:
            l += (self.right.inorder_traverse())
        return l

    def postorder_traverse(self) -> list:
        l = []
        if self.left:
            l += (self.left.postorder_traverse())
        if self.right:
            l += (self.right.postorder_traverse())
        l.append(self.item)
        return l


class BinaryTree:
    def __init__(self, root: Node):
        self.root = root

    def size(self) -> int:
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self) -> int:
        if self.root:
            return self.root.depth()
        else:
            return 0

    def preorder_traverse(self) -> list:
        traverse = []
        if self.root:
            traverse += (self.root.preorder_traverse())
        return traverse

    def inorder_traverse(self) -> list:
        traverse = []
        if self.root:
            traverse += (self.root.inorder_traverse())
        return traverse

    def postorder_traverse(self) -> list:
        traverse = []
        if self.root:
            traverse += (self.root.postorder_traverse())
        return traverse

    def breadth_first_traverse(self) -> list:
        '''너비우선순회'''
        # 재귀적으로 X, 큐 사용
        if not self.root:
            return []

        traversal = []
        q = queue.LinkedListQueue()
        q.enqueue(self.root)

        while not q.isEmpty():
            curr = q.dequeue()
            if curr.left:
                q.enqueue(curr.left)
            if curr.right:
                q.enqueue(curr.right)
            traversal.append(curr.item)
        return traversal


bt = BinaryTree(Node(4))
left_node = Node(2)
left_node.left = Node(1)
left_node.right = Node(3)
right_node = Node(5)
bt.root.left = left_node
bt.root.right = right_node

print(bt.preorder_traverse())
print(bt.inorder_traverse())
print(bt.postorder_traverse())
print(bt.breadth_first_traverse())
