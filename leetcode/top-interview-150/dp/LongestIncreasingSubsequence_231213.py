from typing import List


class Solution:
    # 새로운 아이디어를 떠올리려 하지말고 일단 떠오르는 생각대로 처리할 수 있는지 계산해보기.
    # 1D dp
    # divide and conquer 가능한가?
    def lengthOfLIS_Fail(self, nums: List[int]):
        # 자신보다 작은 값중 가장 오른 인덱스
        # 정렬이 안되어있는데 어떻게 binary serach 가능하지.
        def binary_search(end: int, target: int) -> int:
            lo, hi = 0, end
            ans = end + 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    ans = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans

        dp = [0] * len(nums)
        lis = 0
        for i in range(len(nums)):
            res = binary_search(i - 1, nums[i])
            print("bin", nums[i], nums[res])
            dp[i] = dp[binary_search(i - 1, nums[i])] + 1
            if dp[i] > lis:
                lis = dp[i]
        print(dp)
        return lis

    # O(N^2)
    # dfs with cache => dp인가?
    def lengthOfLIS(self, nums: List[int]):
        dp = [1] * len(nums)
        lis = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            if dp[i] > lis:
                lis = dp[i]

        return lis

    # nums자체는 정렬되어있지 않은 상태로 이진탐색 불가능
    # asceding array를 만들어간다.
    def lengthOfLIS2(self, nums: List[int]):
        def bisect_left(target: int):
            lo, hi = 0, len(arr) - 1
            res = hi + 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] >= target:
                    res = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return res

        arr = [nums.pop(0)]
        for n in nums:
            if n > arr[-1]:
                arr.append(n)
            else:
                arr[bisect_left(n)] = n
        return len(arr)


    # 반례 [4, 10, 4, 3, 8, 9]
    def lengthOfLIS_Fail2(self, nums: List[int]):
        arr = [nums[0]]
        for n in nums:
            if n < arr[-1]:
                arr[-1] = n
            elif n > arr[-1]:
                arr.append(n)
        return len(arr)


# isSubsequence문제와 차이점?
# two pointer로 해결할 수 없음.
def longestCommonSubsequence(text1: str, text2: str) -> int:
    text1 = len()
    j


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(s.lengthOfLIS([1]))

print(s.lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS2([0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS2([7, 7, 7, 7, 7, 7, 7]))
print(s.lengthOfLIS2([1]))
