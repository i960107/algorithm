class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        # insert_after() pop_after() 구현하기 위해 dummy head
        self.head = Node(None)
        self.tail = None
        # tail은 빈 노드가 아니라 None임
        # self.head.next는 Node()시 이미 초기화 되어있으므로 tail 연결할 필요 없음.
        # self.head.next = self.tail
        self.node_count = 0

    def get_length(self) -> int:
        # head는 node로 치지 않음.
        return self.node_count

    def get_at(self, pos: int) -> Node:
        # 맨 앞 원소를 삽입하거나 삭제하는 경우를 위해 dummy head 참조할 필요 있음
        if pos < 0 or pos > self.get_length():
            raise IndexError

        if pos == self.get_length():
            return self.tail

        i = 0
        curr = self.head

        while i < pos:
            i += 1
            curr = curr.next

        return curr

    def traverse(self) -> list:
        curr = self.head
        l = []

        # 다음 원소가 있다면
        while curr:
            l.append(curr.data)
            curr = curr.next
        return l

    # 헤드는 항상 dummy head.따라서 헤드를 조정해줄 필요가 없어서 간단함
    def insert_after(self, prev: Node, new_node: Node) -> bool:
        new_node.next = prev.next
        if not prev.next:
            self.tail = new_node
        prev.next = new_node
        self.node_count += 1
        return True

    # insert_after 호출해서 간단하게 처리가능
    def insert_at(self, pos: int, new_node: Node) -> bool:

        if pos < 1 or pos > self.get_length() + 1:
            return False

        prev = self.get_at(pos - 1)

        return self.insert_after(prev, new_node)

    def pop_after(self, prev: Node) -> int:

        curr = prev.next
        prev.next = curr.next

        if not curr.next:
            if self.node_count == 1:
                self.tail = None
            else:
                self.tail = prev

        self.node_count -= 1

        return curr.data

    def pop_at(self, pos: int) -> int:
        if pos < 1 or pos > self.node_count:
            raise IndexError

        prev = self.get_at(pos - 1)
        return self.pop_after(prev)

    def concat(self, l2) -> None:
        if self.tail:
            self.tail.next = l2.head.next
        else:
            self.head.next = l2.head.next
        if l2.tail:
            self.tail = l2.tail
        self.node_count += l2.node_count
