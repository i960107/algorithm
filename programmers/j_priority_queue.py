import f_doubly_linked_list


class PriorityQueue:

    def __init__(self):
        self.queue = f_doubly_linked_list.DoublyLinkedList()

    def enqueue(self, x):
        # 우선순위 맞춰서 넣어주기. 크기순 오름차순
        newNode = f_doubly_linked_list.Node(x)

        curr = self.queue.head
        while curr.next.next and curr.next.data < x:
            curr = curr.next
        self.queue.insert_after(curr, newNode)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue Empty')

        return self.queue.pop_at(1)

    def size(self) -> int:
        return self.queue.get_length()

    def isEmpty(self) -> bool:
        return self.queue.get_length() == 0

    def peek(self) -> f_doubly_linked_list.Node:
        if self.isEmpty():
            raise IndexError('Queue Empty')

        return self.queue.get_at(1)
