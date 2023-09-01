class StackOverFlowError(RuntimeError):
    pass


class StackUnderFlowError(RuntimeError):
    pass


class Stack:
    # stack에 저장될 수 있는 원소들의 데이터 타입 물어보고 구현 시작하는 것이 좋음.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.top = -1
        self.stack = [None] * capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def push(self, n: int):
        if self.is_full():
            raise StackOverFlowError
        self.size += 1
        self.top += 1
        self.stack[self.top] = n

    def pop(self):
        if self.is_empty():
            raise StackUnderFlowError
        self.size -= 1
        popped = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return popped

    def peek(self):
        return self.stack[self.top]

    # 하나씩 지우기보다 배열 재할당 -> gc에 의해서 기존 배열 메모리에서 제거됨.
    # top만 -1로 내려주면 gc에 의해 지워지지 않음. 메모리에서 깨긋이 지우려면 좋은 방법이 아님.
    def popAll(self):
        self.stack = [None] * self.size


s = Stack(5)

for i in range(6):
    try:
        s.push(i)
    except StackOverFlowError:
        print("stack overflow: ", i, "를 넣지 못하였습니다")

print("stack 상태 : %d/ %d" % (s.size, s.capacity))

for _ in range(6):
    try:
        print(s.pop(), "빠짐")
        print("stack 상태 : %d/ %d" % (s.size, s.capacity))
    except StackUnderFlowError:

        print("stack underflow: ", i, "번째 원소를 빼지 못하였습니다")
