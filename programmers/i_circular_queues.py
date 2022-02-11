import decimal


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
        # 환형 큐에서는 isFull()이 필요
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.is_full():
            raise IndexError('Queue full')

        # 실제로는 한줄인 코드를 편의상 여러줄로 구분할때 \
        # self.rear = 0 \
        #     if self.rear == self.maxCount - 1 \
        #     else self.rear + 1

        # rear 포인터 조정 후 값 삽입
        # 위와 같은 방법이지만 간단하게 표현
        self.rear = (self.rear + 1) % self.maxCount
        # 값 하나 들어갔을때는 front==-1 rear ==0


        self.data[self.rear] = x

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue empty')

        # self.front = 0 \
        #     if self.front == self.maxCount - 1 \
        #     else self.front + 1

        #front 포인터 조정한 후에 값 삭제
        self.front = (self.front + 1) % self.maxCount

        result = self.data[self.front]

        self.count -= 1

        return result

    def peek(self):
        if self.is_empty():
            raise IndexError('Queue empty')

        return self.data[(self.front + 1) % self.maxCount]


q = CircularQueues(3)
q.enqueue(1)
print(f'front {q.front} rear {q.rear}')
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(f'front {q.front} rear {q.rear}')
q.enqueue(4)
print(f'front {q.front} rear {q.rear}')
print(q.dequeue())
print(f'front {q.front} rear {q.rear}')
print(q.dequeue())
print(q.dequeue())
print(f'front {q.front} rear {q.rear}')
