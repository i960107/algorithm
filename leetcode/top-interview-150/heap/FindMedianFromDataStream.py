import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.size = 0

    # minheap maxheap의 길이차가 최대 1
    # 소수점 다섯째짜리까지 정확해야함.
    # 데이터가 아무것도 삽입되지 않아서 중간값이 없을때 중앙값을 조회하는 함수가 호출되지 않음
    # two heaps 써야하는 이유. 넣을때마다 정렬하면? sortedList
    # 2,1이 아닌 1,2로 넣어야하는이유 ?
    # maxheap이 비엇을때,  >일때, ==일때 따로 처리해야함.
    # ==일때와 maxheap이 비었을때 minheap에 넣고, <일때 maxheap에 넣는다.
    # self.minheap이 있는지 체크 안 해주어도됨
    def addNum(self, num: int) -> None:
        if len(self.max_heap) < len(self.min_heap):
            if self.min_heap[0] <= num:
                popped = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -popped)
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        elif len(self.max_heap) == len(self.min_heap):
            if self.min_heap and self.min_heap[0] <= num:
                popped = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -popped)
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)

    def addNumOptimized(self, num: int) -> None:
        # heappushpop()시에 num이 가장 크다면 그 원소가 빠짐.
        # self.min_heap size = self.max_heap size + 1
        # self.max_heap size를 더 크게 하면
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        else:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))

    def findMedian(self) -> float:
        print(self.max_heap, self.min_heap)
        if len(self.max_heap) == len(self.min_heap):
            return (- self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return - self.max_heap[0]


# obj = MedianFinder()
# obj.addNum(-1)
# print(obj.findMedian())
# obj.addNum(-2)
# print(obj.findMedian())
# obj.addNum(-3)
# print(obj.findMedian())
# obj.addNum(-4)
# print(obj.findMedian())
# obj.addNum(-5)
# print(obj.findMedian())
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.max_heap)
print(obj.findMedian())

# obj = MedianFinder()
# obj.addNum(1)
# print(obj.findMedian())
# obj.addNum(2)
# print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())
# obj.addNum(4)
# print(obj.findMedian())
