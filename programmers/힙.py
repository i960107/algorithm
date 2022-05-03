from __future__ import annotations


class BinaryHeap(object):
    '''min heap'''

    def __init__(self):
        # index 0 부터 시작하기 위해(인덱스 계산을 편하게 하기 위해) dummy head 추가
        self.items = [None]

    def __len__(self):
        # len(self.itmes) == 마지막 인덱스
        return len(self.items) - 1

    def heappush(self, val: int):
        '''삽입 - Up-heap'''
        # O(LogN)
        # 배열의 마지막에 삽입한다
        self.items.append(val)
        # 삽입된 위치
        curr = len(self)
        # 부모 값보다 더 작을 경우 부모 노드와 swap한다
        # 계속해서 부모 노드와 비교한다. 루트까지 혹은 자기보다 작은 부모 노드 만날때까지
        while curr // 2 > 0 and self.items[curr // 2] > self.items[curr]:
            self.items[curr // 2], self.items[curr] = self.items[curr], self.items[curr // 2]
            curr = curr // 2

    def heappop(self) -> None | int:
        # O(LogN)
        '''추출 - 가장 작은 값 추출 Down-heap'''
        # 외우기!
        if len(self) < 1:
            return None
        # 루트노드와 마지막 노드 값 바꾸기
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        extracted = self.items.pop()
        # 이진 힙의 성질 유지하도록 루트 노드 자식노드와 비교
        self.heapify(1)
        return extracted

    def heapify(self, index):
        '''index를 루트 노드로 한 이진 힙 구성 '''
        smallest = index
        left, right = index * 2, index * 2 + 1
        # 왼쪽 노드 오른쪽 노드 각각 비교해서 smallest 원소 정하기
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != index:
            # 값 swap 후 재귀 호출
            self.items[smallest], self.items[index] = self.items[index], self.items[smallest]
            self.heapify(smallest)


min_heap = BinaryHeap()
min_heap.heappush(4)
min_heap.heappush(3)
min_heap.heappush(9)
min_heap.heappush(1)
min_heap.heappush(2)
print(min_heap.items)
print(min_heap.heappop())
print(min_heap.items)
