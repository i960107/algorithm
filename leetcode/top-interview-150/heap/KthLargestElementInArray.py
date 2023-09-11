from typing import List
import heapq


class Solution:
    # python은 최소힙만 제공하니깐 값을 반전시켜서 최대힙으로 만들든가
    # len(nums) - k + 1 . 5개 중 2번째로 큰 값은 4번째로 작은값
    # 중복된 값 있을 수 있음. [1,2,3,4,4,5]에서 k =3 이라면 4가 반환되어야함.
    # k가 len(nums) 보다 큰 비정상적인 경우는 입력으로 주어지지 않음
    # nums는 빈 배열일 수 없음
    # without sort. sorting하면 가장 최적화되어있기 때문에 빠름. tim sort c로 구현되어 있기 때문에 매우 빠르다.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        for _ in range(k - 1):
            heapq.heappop(heap)
        return - heapq.heappop(heap)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

    # k개만 큐에 저장하고 더 큰 값이 들어올때만 큐에 넣는다
    # 메모리 측면에서 효율적
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        q = []
        for a in nums:
            if len(q) < k:
                heapq.heappush(q, a)
            else:
                if a > q[0]:
                    heapq.heappushpop(q, a)
        return heapq.heappop(q)


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 3))
print(s.findKthLargest2([3, 2, 1, 5, 6, 4], 3))
