from typing import List


def sortedSquaresFail(nums: List[int]) -> List[int]:
    # 배열이 input일때!! len(nums) < 2인경우 반드시 체크!!!!!!
    if not nums:
        return nums
    if len(nums) == 1:
        return [nums[0] ** 2]

    l, u = 0, len(nums) - 1
    min_positive = -1
    while l <= u:
        mid = l + (u - l) // 2
        if nums[mid] >= 0 and nums[mid - 1] < 0:
            min_positive = mid
            break
        elif nums[mid] >= 0 and nums[mid - 1] >= 0:
            u = mid - 1
        else:
            l = mid + 1

    left, right = min_positive - 1, min_positive

    result = []
    while True:
        if left < 0 and right >= len(nums):
            break
        elif left < 0:
            result.append(nums[right] ** 2)
            right += 1
        elif right >= len(nums):
            result.append(nums[left] ** 2)
            left -= 1
        else:
            if nums[left] + nums[right] < 0:
                result.append(nums[right] ** 2)
                right += 1
            else:
                result.append(nums[left] ** 2)
                left -= 1

    return result


def sortedSquares(nums: List[int]) -> List[int]:
    '''겉에서 부터 들어가기'''
    l, u = 0, len(nums) - 1
    result = []
    # while l<u 이면 둘중에 하나 이동해서  l== u일때 끝남
    # 한 원소 안
    while l <= u:
        # 절대값이 큰 것 부터 추가하기
        if abs(nums[l]) > abs(nums[u]):
            result.append(nums[l] ** 2)
            l += 1
        else:
            result.append(nums[u] ** 2)
            u -= 1

    return result[::-1]


print(sortedSquares([-4, -1, 0, 3, 10]))
print(sortedSquares([0, 3, 10]))
print(sortedSquares([-7, -3, 2, 3, 11]))
print(sortedSquares([1]))
