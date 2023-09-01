from typing import Any


class CircularQueue:
    class EmptyError(Exception):
        pass

    class FullError(Exception):
        pass

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # queue가 가득차 있거나 비어있을때 front == rear
        self.front = 0
        self.rear = 0
        self.queue = [None] * capacity

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    # 배열을 새로 할당
    def dequeue_all(self):
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, n: int):
        if self.is_full:
            raise CircularQueue.FullError
        self.queue[self.rear] = n
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise CircularQueue.EmptyError
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
