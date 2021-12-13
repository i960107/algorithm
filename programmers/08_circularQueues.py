class CircularQueues:
    def __init__(self, n):
        self.data = [None] * n
        self.maxCount = n
        self.count = 0
        self.rear = -1
        self.front = -1

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.is_full():
            raise IndexError('Queue full')

        self.rear = 0 \
            if self.rear == self.maxCount - 1 \
            else self.rear + 1

        self.data[self.rear] = x

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue empty')

        result = self.data[self.front + 1]

        self.front = 0 \
                if self.front == self.maxCount - 1 \
                else self.front + 1

        self.count -= 1

        return result

    def peek(self):
        if self.is_empty():
            raise IndexError('Queue empty')

        return self.data[self.front + 1] if self.front != self.maxCount -1 else self.data[0]
