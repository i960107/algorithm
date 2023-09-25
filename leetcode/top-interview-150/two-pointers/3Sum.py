from typing import List

from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 정렬된 값이 아님...
        nums.sort()

        # 중복값이 있을 수 있음
        # 인덱스 검사 위해 set아닌 dict형이어야함
        # 최대 2번만 가능.
        filtered = []
        count = 0
        for n in nums:
            if filtered and filtered[-1] == n:
                if count >= 2:
                    continue
                filtered.append(n)
                count += 1
            else:
                filtered.append(n)
                count = 1
        print(filtered)

        visited = set()
        result = []
        # 중복된 값이 없도록 (-1, -1, 0) == (0,-1,-1)
        # 어떻게ㅓ
        # (-1, 0, 1) , (-1, 1, 0)

        # visited로 체크해줘도 어쨌든 O(N^2)이 되므로 TLE 발생
        # 9,000,000정도는 괜찮지 않나
        # for i in range(len(filtered)):
        #     for j  in range(i + 1, len(nums)):
        #         target = - ( nums[i] + nums[j])

        #         triplet_id = ' '.join(str(x) for x in sorted([nums[i], nums[j], target]))
        #         if triplet_id in visited:
        #             continue

        #         visited.add(triplet_id)

        #         if target not in num_map:
        #             continue

        #         # 여기서도 중복 일어남.
        #         for k in num_map[target]:
        #             if k == i or k == j:
        #                 continue
        #             result.append([nums[i], nums[j], nums[k]])
        #             break
        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < n and nums[j] == nums[j - 1]:
                        j += 1
                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1
        return answer


s = Solution()
print(s.threeSum2([-1, 0, 1, 2, -1, -4]))
