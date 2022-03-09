from __future__ import annotations
import heapq


class MaxHeap:
    def __init__(self):
        # root index 1부터 시작. index 0에 dummy 원소
        self.data = [None]

    def add(self, key: int):
        '''원소를 삽입하기'''
        # 중복된 원소는 없다고 가정
        self.data.append(key)
        pos = len(self.data) - 1

        while pos // 2 >= 1 and self.data[pos // 2] < key:
            self.data[pos // 2], self.data[pos] = self.data[pos], self.data[pos // 2]
            pos = pos // 2

    def remove(self) -> int | None:
        '''최대 원소(Root node)를 반환 그리고 동시에 이 노드를 삭제'''
        # 매개 변수 없음. root만 삭제가능
        if len(self.data) > 1:
            # 1) 마지막 원소를 root로 끌어올리기.삭제도 가장 마지막에서만 일어나야 완전 이진 트리의 모습을 유지할 수 있음.
            self.data[-1], self.data[1] = self.data[1], self.data[-1]
            # 2) 마지막 원소(가장 큰 값)를 꺼냄
            data = self.data.pop(-1)
            # 3) 임시로 root에 넣어둔 원소의 인덱스를 maxheap을 만족할때까지 조정
            self.maxheapify(1)
        else:
            data = None
        return data

    def heap_sort(self) -> list:
        '''remove()를 반복함으로써 데이터를 정렬 - 힙 정렬하기'''
        sorted = []
        while len(self.data) > 1:
            sorted.append(self.remove())
        return sorted

    def maxheapify(self, i: int) -> None:
        '''index i 노드를 이동해서 최대 힙 만들기-재귀적 구현'''
        # 인덱스 참조한 결과가 아니라 인덱스를 변수로 지정. 재활용하도록
        left = i * 2
        right = i * 2 + 1
        biggest = i
        # 자식들 중 더 큰 키 값을 가지는 노드를 찾아서.
        if left < len(self.data) and self.data[left] > self.data[biggest]:
            biggest = left
            # i를 biggest로 조정하면안됨. 원래 값에서 변했는지 안 변했는지 알 수 있어야 함.
            # i = left
        # elif 아니고 if. 위에서 왼쪽 자식과 바꾸었더라도 오른쪽 자식과 비교해 최대 원소가 위에 올라오도록
        if right < len(self.data) and self.data[right] > self.data[biggest]:
            biggest = right
        # 재귀 호출은 언제 끝나나? i==biggest일때. i를 루트로한 서브트리가 맥스힙일때.
        if i != biggest:
            self.data[i], self.data[biggest] = self.data[biggest], self.data[i]
            # i에 대해서 아니고 biggest -> 바뀐 원소를 루트로 heapify호출
            self.maxheapify(biggest)


h = MaxHeap()
h.add(24)
h.add(21)
h.add(18)
h.add(30)
h.add(19)
h.add(4)
h.add(2)
h.add(12)
h.add(8)
h.add(6)
print(h.heap_sort())

# ----------------------heapq 모듈을 이용 ------------------

'''heapq 모듈을 이용한 우선순위 큐 구현- minheap'''

l = [4, 1, 7, 3, 8, 5]
# heapq 모듈에서는 값이 작을수록 우선순위가 큰 min heap
# list를 min heap으로 변환.반환값 없음

# O(NlogN)
heapq.heapify(l)
print(l)

# 오름차순으로 꺼내기 O(NlogN)

min_heap = []
while l:
    min_heap.append(heapq.heappop(l))
print(min_heap)

# 가장 작은 원소 얻기 O(1)
min = min_heap[0]
print(f'min {min}')

'''heapq모듈을 이용한 우선순위 큐  구현 - maxheap 구현'''
# heapq 모듈은 min heap 만 지원하므로 응용필요.

l2 = [4, 1, 7, 3, 8, 5]
priorityQ = []

# 각 원소에 대한 우선순위를 구한 후 하나씩 heappush - >heapify
# 리스트와 튜플 둘다 순서를 관리하지만, 리스트는 mutable 튜플은 immutable - 수정 불가
# O(NlogN)
for element in l2:
    heapq.heappush(priorityQ, (-element, element))  # (우선순위, 값) - 값이 클수록 우선순위 높음

print(priorityQ)

# O(NlogN)
# 가장 큰 원소부터 하나씩 가져오기
max_heap = []
while priorityQ:
    max_heap.append(heapq.heappop(priorityQ)[1])

print(max_heap)

'''k번째 최소값 구하기'''


def kth_smallest(nums: list, k: int) -> int:
    heapq.heapify(nums)

    kth_min = None
    for _ in range(k):
        # k번 꺼내기
        kth_min = heapq.heappop(nums)
    return kth_min


l3 = [4, 1, 7, 3, 8, 5]
print(f'3번째로 작은 값 {kth_smallest(l3, 3)}')

'''k번째 최대값 구하기'''


def kth_largest(nums: list, k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, (-num, num))

    kth_max = None
    for _ in range(k):
        # k번 꺼내기
        kth_max = heapq.heappop(heap)[1]
    return kth_max


l4 = [4, 1, 7, 3, 8, 5]
print(f'3번째로 큰 값 {kth_largest(l4, 3)}')
