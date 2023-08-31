from typing import List
from collections import Counter


class Solution:
    # sliding window -> non duplicated substring
    # 연속된 부분이 아니어도됨.
    # 그냥 바로 뒤에서 시작하면됨.
    # 정렬되지 않은 리스트  O(N) 시간복잡도 내에 해결해야하므로 정렬할 수 없음.
    # linked list를 사용해볼까
    # 중복된 원소 포함하는가.
    def longestConsecutive(self, nums: List[int]) -> int:
        # left = right = 0
        # maxLen = 0
        # for i, n in enumerate(nums):
        #     if i == 0 or nums[i] == nums[i - 1] + 1:
        #         right += 1
        #     else:
        #         if right - left > maxLen:
        #             maxLen = right - left
        #         left = right

        # linkedlist를 arr로 나타내기. 별도의 클래스 만들필요 없이.
        # counts = Counter(nums)
        # d = dict()
        # for n in nums:
        #     if n - 1 in d:
        #         d[n - 1] = n
        #
        #     if n + 1 in d:
        #         d[n] = n + 1
        #     else:
        #         d[n] = None

        # 어떻게 가장 긴 길이를 뽑아낼것인가.
        # 한번 방문한 곳 제거하면 안됨. 그 다음에 검색된 길이가 더 길 수 있음
        # for n in d:
        #     curr = n
        #     length = 0
        #
        #     while curr and curr not in visited:
        #         length += 1
        #         curr = d[curr]
        #         visited.add(curr)
        #
        #     if length > max_length:
        #         max_length = length

        max_length = 0
        consecutive_lengths = dict()
        # 이전에 값이 갱신이 안됨 0등장후 1 ~9 탐색되었을때..
        # 123 567 후 4가 등장했을때.

        # for n in d:
        #     if n + 1 in consecutive_lengths:
        #         consecutive_lengths[n] = consecutive_lengths[n + 1] + counts[n]
        #     else:
        #         curr = n
        #         length = 0
        #         while curr:
        #             length += counts[curr]
        #             curr = d[curr]
        #         consecutive_lengths[n] = length
        #     if consecutive_lengths[n] > max_length:
        #         max_length = consecutive_lengths[n]
        # print(d)
        # print(counts.items())
        # print(consecutive_lengths)
        # return max_length

        #     while curr and curr not in visited:
        #         length += 1
        #         curr = d[curr]
        #         visited.add(curr)
        #
        #     if length > max_length:
        #         max_length = length

        # 그래프의 disjoint set을 활용?
        # 공간이 많이 사용됨.
        numbers = set(nums)
        consecutive_lengths = dict()
        max_length = 0
        for n in numbers:
            if n in consecutive_lengths:
                continue
            curr = n
            while curr - 1 in numbers:
                curr = curr - 1

            length = 0
            while curr in numbers:
                length += 1
                consecutive_lengths[curr] = length
                curr = curr + 1
            if max_length < length:
                max_length = length
        return max_length

    # 공간 복잡도를 줄일 수 있음
    # consecutive lengths를 기억할 필요 없음
    def solution(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            curr = num
            l = 0
            while curr in nums_set:
                l += 1
                curr += 1
            if l > max_len:
                max_len = l
        return max_len


s = Solution()
print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(s.longestConsecutive(nums=[4, 2, 3, 1, 5]))
