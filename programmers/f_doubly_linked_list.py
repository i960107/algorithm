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
        # dummy tail을 제외하기 위해서 curr.next.next의 유효성을 확인
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
        # dummy head와 dummy tail을 참조할 때 있음
        if pos < 0 or pos > self.get_length() + 1:
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

    def insert_after(self, prev: Node, new_node: Node) -> bool:
        next_node = prev.next
        new_node.next = next_node
        new_node.prev = prev
        prev.next = new_node
        next_node.prev = new_node
        self.node_count += 1
        return True

    def insert_before(self, next_node: Node, new_node: Node) -> bool:
        prev = next_node.prev
        new_node.prev = next_node.prev
        new_node.next = prev.next
        prev.next = new_node
        next_node.prev = new_node
        self.node_count += 1
        return True

    def insert_at(self, pos: int, new_node: Node) -> bool:
        if pos < 1 or pos > self.get_length() + 1:
            return False

        prev = self.get_at(pos - 1)

        return self.insert_after(prev, new_node)

    def pop_after(self, prev: Node) -> int:
        curr = prev.next
        next_node = curr.next
        prev.next = next_node
        curr.prev = prev
        self.node_count -= 1
        return curr.data

    def pop_before(self, next_node: Node) -> int:
        curr = next_node.prev
        prev = curr.prev
        prev.next = next_node
        next_node.prev = prev
        self.node_count -= 1
        return curr.data

    def pop_at(self, pos: int) -> int:
        if pos < 1 or pos > self.get_length():
            raise IndexError

        prev = self.get_at(pos - 1)

        return self.pop_after(prev)

    def concat(self, l2):
        if l2.node_count == 0:
            return
        self.tail.prev.next = l2.head.next
        l2.head.next.prev = self.tail.prev
        self.tail = l2.tail
        self.node_count += l2.node_count
