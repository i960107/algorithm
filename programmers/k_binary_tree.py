class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        # 인덱스 역할을 할 key 없어도 되나보지?
        self.data = item


class BinaryTree:
    '''이진 트리의 추상적 자료구조 구현'''
    def __init__(self):
        self.root = None

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        pass

    def postorder(self):
        pass

    def bfs(self):
        if not self.root:
            return []

        traversal = []

        queue = LinkedListQueue()
        queue.put(self.root)

        while not queue.is_empty:
            curr = queue.get()
            traversal.append(curr.data)
            if curr.left:
                queue.put(curr.left)
            if curr.right:
                queue.put(curr.right)

        return traversal
