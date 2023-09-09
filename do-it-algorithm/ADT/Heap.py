class Heap:
    def __init__(self, capacity: int):
        self.arr = []
        self.n = 0
        self.capacity = capacity

    def push(self, num: int):
        if self.n == self.capacity:
            raise RuntimeError("Heap Overflow")
        self.arr.append(num)
        self.bubble_up(self.n)
        self.n += 1

    def bubble_up(self, i: int):
        # levle2  이상부터 수행됨
        while ((i - 1) // 2) >= 0:
            p = (i - 1) // 2
            if self.arr[p] < self.arr[i]:
                self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
                i = p
            else:
                break

    # 만약 원소가 하나라면?
    # bubble_down()바로 종료됨
    def pop(self) -> int:
        if self.n == 0:
            raise RuntimeError("Heap Underflow")

        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.n -= 1
        result = self.arr.pop()

        self.bubble_down(0)

        return result

    # 중복된 값이 있는 경우?
    def bubble_down(self, i: int):
        curr = i
        while curr < self.n:
            left = curr * 2 + 1 if curr * 2 + 1 < self.n else None
            right = curr * 2 + 2 if curr * 2 + 2 < self.n else None

            if left and self.arr[left] > self.arr[curr]:
                # 둘다 큰 경우 둘 중 큰거
                if right and self.arr[right] > self.arr[left]:
                    self.arr[curr], self.arr[right] = self.arr[right], self.arr[curr]
                    curr = right
                else:
                    self.arr[curr], self.arr[left] = self.arr[left], self.arr[curr]
                    curr = left
            elif right and self.arr[right] > self.arr[curr]:
                self.arr[curr], self.arr[right] = self.arr[right], self.arr[curr]
                curr = right
            else:
                break

    def heapifiy(self):
        for i in range((self.n - 2) // 2, -1, - 1):
            self.bubble_down(i)

    def is_empty(self) -> bool:
        return self.n == 0


heap = Heap(20)
heap.push(20)
heap.push(4)
heap.push(8)
heap.push(10)
heap.push(5)
heap.push(7)
heap.push(6)
heap.push(2)
heap.push(9)
heap.push(1)

while not heap.is_empty():
    print(heap.pop())
