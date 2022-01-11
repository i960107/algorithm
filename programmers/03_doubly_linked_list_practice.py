class Node:
    def __init__(self, data: int):
        self.data = data
        # Node(None)아님. maximum recursion depth exceeded
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        self.head.prev = None
        self.head.next = self.tail

        self.tail.prev = self.head
        self.tail.next = None

        self.node_count = 0

    def get_length(self) -> int:
        return self.node_count

    def traverse(self) -> list:
        l = []
        curr = self.head
        # curr.next? tail None 출력. 맨 마지막 원소 출력 안될거라고 생각했는데?
        # self.head부터시작해서curr.next.next있으면 curr.next원소를 리스트에 추가하는 방식
        # 빈 배열인 경우? curr.next 존재
        while curr.next.next:
            curr = curr.next
            # l += curr.data
            #  + 원소 추가는 안됨. 리스트 병합시 사용
            l.append(curr.data)
        return l

    def reverse(self) -> list:
        l = []
        curr = self.tail
        # curr.prev? head None 출력됨
        while curr.prev.prev:
            curr = curr.prev
            l.append(curr.data)
        return l

    def get_at(self, pos: int) -> Node:
        # 삽입 삭제시 prev 만 구하기 때문에 get_length까지 필요
        if pos < 0 or pos > self.get_length():
            raise IndexError
        if pos < (self.get_length()) // 2:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
        else:
            i = 0
            # tail에서부터 찾아갈때 인덱스 계산 주의!!
            # 뒤에서부터 인덱스매기기
            curr = self.tail
            while i < self.get_length() + 1 - pos:
                curr = curr.prev
                i += 1
        return curr

    def concat(self, l2) -> None:
        # 주의
        if l2.node_count == 0:
            return
        original_end = self.tail.prev
        original_end.next = l2.head.next
        l2.head.next.prev = original_end
        l2.tail.prev.next = self.tail
        self.tail.prev = l2.tail.prev
        self.node_count += l2.node_count

    def insert_after(self, prev: Node, new_node: Node) -> bool:
        new_node.next = prev.next
        prev.next = new_node
        new_node.next.prev = new_node
        new_node.prev = prev
        # 헤드 조정 필요 없음
        self.node_count += 1
        return True

    def insert_at(self, pos: int, new_node: Node) -> bool:
        # get_length+1 즉, 제일 마지막에 추가할 수 있음
        if pos < 1 or pos > self.get_length() + 1:
            return False
        prev = self.get_at(pos - 1)
        return self.insert_after(prev, new_node)

    def insert_before(self, next: Node, new_node: Node) -> bool:
        new_node.next = next
        next.prev.next = new_node
        new_node.prev = next.prev
        next.prev = new_node
        self.node_count += 1
        return True

    def pop_after(self, prev: Node) -> int:
        curr = prev.next
        prev.next = curr.next
        curr.next.prev = prev
        self.node_count -= 1
        return curr.data

    def pop_before(self, next: Node) -> int:
        curr = next.prev
        prev = curr.prev
        prev.next = next
        next.prev = prev
        self.node_count -= 1
        return curr.data

    def pop_at(self, pos: int) -> int:
        if pos < 1 or pos > self.get_length():
            raise IndexError
        prev = self.get_at(pos - 1)
        return self.pop_after(prev)


dl = DoublyLinkedList()
dl.insert_at(1, Node(1))
dl.insert_at(2, Node(2))
dl.insert_at(3, Node(3))
dl.insert_at(4, Node(4))
dl.insert_before(dl.get_at(4), Node(3))
print(dl.traverse())
print(dl.reverse())
print(dl.pop_before(dl.get_at(4)))
dl2 = DoublyLinkedList()
# # dl2.insert_at(1, Node(10))
# dl2.insert_at(2, Node(20))
# dl2.insert_at(3, Node(30))
# dl2.insert_at(4, Node(40))
dl2.concat(dl)
print(dl2.traverse())
