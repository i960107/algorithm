from typing import List


class Solution:
    # a, b inclusive list[a:b+1]
    # 정렬된 배열, 중복 값 없음
    # 빈 배열일 수 있음. 음수 포함.
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 앞쪽으로 살피는게 좋을까 뒤로 살피는게 좋을까?
        result = []
        temp = []
        for i, n in enumerate(nums):
            # 이전과 값이 연속되거나 불연속되거나
            # temp에 값이 차있다는 것은
            if i == 0 or nums[i - 1] + 1 == n:
                if len(temp) < 2:
                    temp.append(n)
                else:
                    temp[-1] = n
            elif nums[i - 1] + 1 != n:
                if len(temp) == 1:
                    result.append(str(temp[0]))
                elif len(temp) == 2:
                    result.append('->'.join(str(x) for x in temp))
                temp = [n]

                # len(temp) <= 2
        if len(temp) == 1:
            result.append(str(temp[0]))
        elif len(temp) == 2:
            result.append('->'.join(str(x) for x in temp))
        return result

    def summaryRanges2(self, nums: List[int]) -> List[str]:
        left, right = 0, 0
        result = []
        while left < len(nums):
            while right + 1 < len(nums) and nums[right + 1] == nums[right] + 1:
                right += 1

            if left != right:
                result.append('%d->%d' % (nums[left], nums[right]))
            else:
                result.append(str(nums[left]))

            left = right + 1
            right = left

        return result


s = Solution()
print(s.summaryRanges2([0, 1, 2, 4, 5, 7]))
print(s.summaryRanges2([0, 2, 3, 4, 6]))
print(s.summaryRanges2([]))
