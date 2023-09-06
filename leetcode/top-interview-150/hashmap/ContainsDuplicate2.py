from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        d = dict()

        for i, n in enumerate(nums):
            if n in d:
                if abs(d[n] - i) <= k:
                    return True
            d[n] = i
        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)

        for num, indices in d.items():
            if len(indices) < 2:
                continue
            for i in range(1, len(indices)):
                if indices[i] - indices[i - 1] <= k:
                    return True
        return False

        # 만약 원소의 값이 모두 가은 10^5  길이의 length가 있다면.
        # list -> set으로
        # i - j = k가 아니라 abs(i-j) <=k
        # 비교시 O(N^2) 되는 거 아닌가..
        # 정렬된 상태여야함...
        # d에 추가된 인덱스는 오름차순 정렬된 상태 -> stack처럼 마지막 원소랑만 비교하면됨...
        # for n, indices in d.items():
        #     if len(indices) < 2:
        #         continue
        #     for i in indices:
        #         if k - i in indices:
        #             return True
        # return False


s = Solution()
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
