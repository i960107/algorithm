# 중복된 원소 최대 2번까지
# 별도의 array 선언할 수 없고 배열을 in-place에서 조작해야하는 문제의 제약사항 상 공간 복잡도는 O(1)이.
# 각 원소가 등장한 횟수를 기록해야한다.
# 만약 길이가 1이라면 for문을 돌지 않고 index 1이 반환된다.
# count를 언제 초기화해주어야하나.
class Solution(object):
    def removeDuplicates(self, nums):
        pos = 1
        count = 1
        for i in range(1, len(nums)):
            # 3번째 중복된 원소인 경우
            if nums[i - 1] != nums[i]:
                nums[pos] = nums[i]
                pos += 1
                count = 1
            else:
                if count < 2:
                    # 두번째 중복 원소이거나, 중복되지 않은 원소인 경우
                    nums[pos] = nums[i]
                    pos += 1
                count += 1

        return pos


s = Solution()
s.removeDuplicates([0, 0, 1, 1, 1, 2, 3, 3])
