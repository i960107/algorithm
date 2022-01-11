class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # AttributeError발생
        # 필요 없음.
        # self.head.next = self.tail
        self.head.next = self.tail
        self.node_count = 0

    def get_length(self) -> int:
        return self.node_count

    def traverse(self) -> list:
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def get_at(self, pos: int) -> Node:
        if pos < 1 or pos > self.node_count:
            raise IndexError

        i = 0
        curr = self.head

        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insert_at(self, pos: int, new_node: Node) -> bool:
        if pos < 1 or pos > self.get_length() + 1:
            return False

        if pos == 1:
            new_node.next = self.head.next
            self.head = new_node
        else:
            prev = self.get_at(pos - 1)
            new_node.next = prev.next
            prev.next = new_node
            if pos == self.node_count + 1:
                self.tail = new_node

        self.node_count += 1

        return True

    def pop_at(self, pos: int, new_node: Node) -> int:
        if pos < 1 or pos > self.get_length():
            raise IndexError

        if pos == 1:
            curr = self.head
            self.head = curr.next
        else:
            prev = self.get_at(pos - 1)
            curr = prev.next
            if pos == self.node_count:
                self.tail = prev

        self.node_count -= 1

        return curr.data

    def concat(self, l2) -> None:
        # linked list 원소가 하나인 경우 head는 원소 있고 tail(None)을 가리킴
        if l2.node_count == 0:
            return
        self.tail.next = l2.head
        self.tail = l2.tail
        if self.node_count == 0:
            self.head = l2.head

        self.node_count += l2.node_count


linked_list = LinkedList()
linked_list2 = LinkedList()
linked_list2.insert_at(1, Node(1))
linked_list2.insert_at(2, Node(2))
linked_list2.insert_at(3, Node(3))

# 빈 리스트 + 리스트
linked_list.concat(linked_list2)
print('test case 1')
print(linked_list.traverse())

#  리스트 + 빈 리스트
linked_list2.concat(linked_list)
print('test case 2')
print(linked_list2.traverse())

# 리스트 + 리스트
linked_list2.concat(linked_list2)
print('test case 3')
print(linked_list2.traverse())
