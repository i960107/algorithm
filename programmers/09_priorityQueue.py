from 03_doublyLinkedList import Node, DoublyLinkedList


class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, x):
        newNode = Node(x)

        curr = self.queue.head
        while curr.next.next and curr.next.data < x:
            curr = curr.next
        self.queue.insert_after(curr, newNode)

        self.queue.nodeCount += 1

    def dequeue(self):
        if self.queue.nodeCount == 0:
            raise IndexError('Queue Empty')

        return self.queue.pop_at(1).data

