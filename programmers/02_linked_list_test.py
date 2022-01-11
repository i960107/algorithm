class Node:
    def __init__(self):
        self.data = None
        self.next = None


class nextdList:
    def __init__(self):
        # tail도 필요. 필요성 get_at() 참고
        self.head = None
        self.tail = None
        self.node_count = 0

    def __str__(self):
        if self.node_count == 0:
            return 'LinkedList : Empty'
        s = ''
        curr = self.head
        while curr:
            s += str(curr.data)
            if curr.next:
                s += ' ->'
            curr = curr.next
        return s

    def get_length(self) -> int:
        return self.node_count

    # 결과 true/false로 반환
    def insert_at(self, pos: int, new_node: Node) -> bool:
        if pos < 1 or pos > self.get_length() + 1:
            return False

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            # tail을 활용해서 특정 원소 참조 최적화
            prev = self.get_at(pos - 1) if pos != self.get_length() + 1 else self.tail
            new_node.next = prev.next
            prev.next = new_node
            if pos == self.get_length() + 1:
                self.tail = new_node
        self.node_count += 1
        return True

    def pop_at(self, pos: int) -> int:
        if pos < 1 or pos > self.get_length():
            raise IndexError

        if pos == 1:
            curr = self.head
            self.head = curr.next
        else:
            prev = self.get_at(pos - 1)
            curr = prev.next
            prev.next = curr.next
            if pos == self.get_length():
                self.tail = prev

        self.node_count -= 1

        return curr.data

    # 자기 자신을 자료형으로 받을 수 없음?
    # 자기 자신을 반환하기?
    # index 를 0부터 시작하는 이유
    # 이후에 dummy head 를 위한 index 0 비워두기
    # 마지막 index가 node_count랑 같다
    def concat(self, l2) -> None:
        # node_count가 인 경우 self.head.next = None, self.tail = self.head?
        self.tail.next = l2.head
        if l2.tail:
            self.tail = l2.tail
        self.node_count += l2.node_count

    def get_at(self, pos: int) -> Node:
        # index는 1부터 시작. 0으로 시작할때에 비해서 뭐가 좋지?
        # 원소의 맨 앞 또는 맨 뒤에 새로운 원소를 삽입/삭제하는 경우
        if pos < 1 or pos > self.get_length():
            raise IndexError

        # 원소가 tail인 경우 O(1)로 바로 반환 가능
        if pos == self.get_length():
            return self.tail

        i = 1
        curr = self.head

        while i < pos:
            i += 1
            curr = curr.next

        return curr

    def traverse(self) -> list:
        curr = self.head
        l = []

        while curr:
            l.append(curr.data)
            curr = curr.next
        return l
