

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.data = item

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        l = self.left.dpeth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return l + 1 if l >= r else r + 1

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        pass

    def postorder(self):
        pass


class BinaryTree:
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
