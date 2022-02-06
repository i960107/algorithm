import f_doubly_linked_list


class LinkedListQueue:
    def __init__(self):
        self.data = f_doubly_linked_list.DoublyLinkedList()

    def enqueue(self, item) -> bool:
        self.data.insert_at(self.data.get_length() + 1, f_doubly_linked_list.Node(item))
        return True

    def dequeue(self):
        # Node 반환
        return self.data.pop_at(1)

    def peek(self):
        # Node안 데이터 반환
        # 만약 queue비었는데 꺼내려고 하면? doublyLinkedList 구현에 의해서 IndexError발생하지 않고 None반환?
        # IndexError발생하는 경우 없음. 항상 index 1을 꺼내는데 빈 연결리스트도 index 1에 tail 존재
        return self.data.get_at(1).data

    def size(self):
        return self.data.get_length()

    def isEmpty(self):
        return self.size() == 0


queue = LinkedListQueue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.peek())
