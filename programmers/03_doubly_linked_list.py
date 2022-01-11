class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodeCount = 0

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList : empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += '->'
        return s

    def traverse(self):
        curr = self.head
        result = []
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def reverse(self):
        curr = self.tail
        result = []
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    def get_length(self):
        return self.nodeCount

    def get_at(self, pos):
        if pos < 1 or pos > self.getLength():
            raise IndexError

        if pos < self.get_length() // 2:
            curr = self.head
            i = 0
            while i < pos:
                curr = curr.next
                i += 1
        else:
            curr = self.tail
            i = 0
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1

        return curr

    def insert_after(self, prev, newNode):
        next = prev.next
        prev.next = newNode
        next.prev = newNode
        newNode.prev = prev
        newNode.next = next
        self.nodeCount += 1
        return True

    def insert_at(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount:
            return False

        prev = self.get_at(pos - 1)
        return self.insert_after(prev, newNode)

    def pop_after(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data

    def pop_at(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError('Index out of range')

        prev = self.get_at(pos - 1)
        return self.pop_after(prev)

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount
