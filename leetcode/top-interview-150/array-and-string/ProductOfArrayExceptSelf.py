from typing import List


class Solution:
    # O(N) without using division operation
    # 0이 섞여있을 경우에 문제임..
    # O(1) extra space compexity. output array 제외하고.
    # 배열을 입력받아 ouput[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하는 것.
    # 나눗셈을 하지않고 O(N)에 풀이하라.
    # 자기 자신을 제외하고 왼쪽의 곱셈결과와 오른쪽의 곰셉결과를 곱한다.
    # out에 왼쪽 곱셈결과를 먼저 추가하고 오른쪽 곱셈결과를 곱한다.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [None] * n
        left_product[0] = 1
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        right_product = [None] * n
        right_product[-1] = 1
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        result = []
        for left, right in zip(left_product, right_product):
            result.append(left * right)
        return result

        # divide and conquer 패턴을 사용할 수 없는 이유
        # divide adn conquer을 언제 사용할 수 있나? -> 전체를 더하고
        # def productExceptSelfDivide(self, nums: List[int]) -> List[int]:
        #     result = [None] * len(nums)
        #
        #     def divide(lo: int, hi: int) -> int:
        #         if lo > hi:
        #             return 1
        #         if lo == hi:
        #             return nums[lo]
        #         mid = (lo + hi) // 2
        #         left = divide(lo, mid - 1)
        #         right = divide(mid + 1, hi)
        #         result[mid] = left * right
        #         return left * right * nums[mid]
        #
        #     divide(0, len(nums) - 1)
        #     return result

    # space complexity O(1)
    def productExceptSelfOptimized(self, nums: List[int]) -> List[int]:
        ans = []
        prefx = 1
        for num in nums:
            ans.append(prefx)
            prefx *= num
        postfx = 1
        for i in range(len(nums) - 1, -1, -1):
            # next postfix value * previous prefixvalue
            ans[i] = ans[i] * postfx
            postfx *= nums[i]
        return ans


s = Solution()
print(s.productExceptSelfOptimized([1, 2, 3, 4]))
print(s.productExceptSelfOptimized([-1, 1, 0, -3, 3]))
