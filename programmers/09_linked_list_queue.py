from 03_doublyLinkedList import Node, DoublyLinkedList


class LinkedListQueue:
    def __init__(self):
        self.data = DoublyLinkedList

    def qsize(self):
        return self.data.get_length()

    def is_empty(self):
        return self.data.get_length() == 0
    def put(self, item):
        newNode = Node(item)
        return self.data.insert_at(self.data.get_length() + 1, newNode)

    def get(self):
        return self.data.pop_at(1)

    def peek(self):
        return self.data.get_at(1).data
