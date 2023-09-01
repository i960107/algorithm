from typing import List


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class LinkedListCircularQueue:
    class EmptyError(Exception):
        pass

    # capacity가 제한되어있지 않음. 큐의 크기를 예측하기 어려울때 사용
    def __init__(self):
        self.size = 0
        self.tail = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # 배열을 새로 할당
    def dequeue_all(self):
        self.tail = None
        self.size = 0

    def enqueue(self, n: int):
        new_node = ListNode(n, None)
        if self.is_empty():
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise LinkedListCircularQueue.EmptyError

        result = None
        if self.size == 1:
            result = self.tail
        else:
            head = self.tail.next
            result = head
            self.tail.next = head.next
        self.size -= 1
        return result


queue = LinkedListCircularQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("recently enqueued : %d" % (queue.tail.val))
print("total size: %d" % (queue.size))

print(queue.dequeue().val)
print(queue.dequeue().val)
print(queue.dequeue().val)
print(queue.dequeue().val)
try:
    print(queue.dequeue())
except:
    print("empty error 발생")

queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(1)

print(queue.dequeue().val)
print(queue.dequeue_all())
