from typing import List


class Solution:
    # O(N^3)?
    # i < j < k인 조건이 영향을 미치나? 정렬을 하면 안되나?
    # 시간초과 어떻게 줄이지?
    def maximumTripletValue_Fail(self, nums: List[int]) -> int:
        # 자신 보다 오른쪽에서 가장 큰 값.
        max_nums = [None] * len(nums)
        max_nums[-1] = nums[-1]

        min_nums = [None] * len(nums)
        min_nums[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if max_nums[i + 1] < nums[i]:
                max_nums[i] = nums[i]
            else:
                max_nums[i] = max_nums[i + 1]
            if min_nums[i + 1] > nums[i]:
                min_nums[i] = nums[i]
            else:
                min_nums[i] = min_nums[i + 1]

        ans = 0
        for i in range(len(nums) - 2):
            if min_nums[i + 1] >= nums[i]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if nums[i] <= nums[j]:
                    continue
                res = (nums[i] - nums[j]) * max_nums[j + 1]
                if res > ans:
                    ans = res
                # 정렬되지 않은 배열에서 어떻게 nums[k]의 최대값을 찾는가.
                # 자신보다 오른쪽에서 가장 큰 값.
        return ans

    def maximumTripletValue_Fail(self, nums: List[int]) -> int:
        pass

    # max_nums = [(n, i) for i, n in enumerate(nums)]
    # min_nums = [(n, i) for i, n in enumerate(nums)]
    # for i in range(len(nums) - 2, -1, -1):
    #     if max_nums[i][0] < max_nums[i + 1][0]:
    #         max_nums[i] = max_nums[i + 1]
    #     if min_nums[i][0] > min_nums[i + 1][0]:
    #         min_nums[i] = min_nums[i + 1]
    # # 만약 j가 마지막 원소라면 j_value가 최소원소가 아니라도 고려해야하는데.
    # for i in range(len(nums) - 2):
    #     i_value = nums[i]
    #     j_value, j = min_nums[i + 1]
    #     # if j ==
    #         max_nums[j + 1]

    def maximumTripletValue2(self, nums: List[int]) -> int:
        # multidimentional_dp ? prefix_sum?
        # max_nums[i] = 0에서 i까지 가장 큰 값.
        # 어떤 수를 기준으로 하냐에 따라 다름.! ( x - y ) * z 일때 y를 기준 혹은 z를 기준으로 할 수 있음
        max_nums = [[n, n] for n in nums]
        for i in range(1, len(nums)):
            if nums[i] < max_nums[i - 1][0]:
                max_nums[i][0] = max_nums[i - 1][0]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < max_nums[i + 1][1]:
                max_nums[i][1] = max_nums[i + 1][1]
        # j를 기준으로 생각.
        # 왜 위의 풀이는 실패했는데 이 풀이는 되지 -> 무조건 왼쪽에서 가장 큰값, 오른쪽에서 가장 큰값 구하면 됨.
        # 위의 풀이는 x가 고정되어 있을때, y가 가장 작지 않아도 z가 더 크면 가능.
        #  i + 1 ~ 끝까지 원소 중 가장 큰 값 -> 뒤에서부터 누적하면 됨!

        max_value = 0
        for j in range(1, len(nums) - 1):
            value = (max_nums[j - 1][0] - nums[j]) * max_nums[j + 1][1]
            if value > max_value:
                max_value = value
        return max_value

    def maximumTripletValue(self, nums: List[int]) -> int:
        max_num = 0
        ans = 0
        max_diff = 0
        for n in nums:
            if max_diff * n > ans:
                ans = max_diff * n

            # maxdiff와 maxnum 갱신 순서는 상관없음
            if n > max_num:
                max_num = n

            if max_num - n > max_diff:
                max_diff = max_num - n

        return ans


s = Solution()
print(s.maximumTripletValue([12, 6, 1, 2, 7]))
print(s.maximumTripletValue([1, 2, 3]))
print(s.maximumTripletValue([3, 2, 99]))
print(s.maximumTripletValue([1, 10, 3, 4, 19]))
