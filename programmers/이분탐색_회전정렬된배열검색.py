from typing import List


# def solution_pivot(nums: List[int], target: int) -> int:
#     '''피벗을 기준으로 한 이진 검색'''
#     # O(NlogN)
#     original = sorted(nums)
#
#     # O(logN)
#     left = 0
#     right = len(nums) - 1
#     location = -1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if original[mid] > target:
#             right = mid - 1
#         elif original[mid] < target:
#             left = mid + 1
#         else:
#             location = mid
#             break
#
#     # O(N^2) min 이 내부적으로 최적화하기 위해 정렬한 후에 최소값을 찾느냐? 아님.선형탐색
#     # pivot = nums.index(min(nums))
#
#     # nums 가 정렬된게 아니기 때문에 이진탐색으로 pivot 구할 수 없음
#     # 최솟값을 찾아 피벗 설정
#     left, right = 0, len(nums) - 1
#     pivot = -1
#     while left < right:
#         mid = left + (right - left) // 2
#         # 정렬되지 않은 상태?
#         if nums[mid] > nums[right]:
#             left = mid + 1
#         else:
#             right = mid
#
#     return location + pivot if location != -1 and pivot != -1 else -1

def solution_pivot(nums: List[int], target: int) -> int:
    '''피벗을 기준으로 한 이진 검색'''
    # 예외 처리
    if not nums:
        return -1

    # 최솟값 찾아 피벗 설정
    # O(N^2) min 이 내부적으로 최적화하기 위해 정렬한 후에 최소값을 찾느냐? 아님.선형탐색
    # pivot = nums.index(min(nums))
    # nums 가 정렬된게 아니기 때문에 이진탐색으로 pivot 구할 수 없음
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        # left+1 = right인 경우 left = mid
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # nums[mid] <= nums[right] 보다 작거나 같은 경우
            right = mid
    pivot = left

    # 정렬된 리스트에서 타겟 원소의 위치 찾기
    # 아니고 pivot을 활용해 피봇된 배열에서 이진 검색하기!!
    # left,right도 pivot된 인덱스 구할 필요 없음. 미드값만 조정해주기
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_pivot = (mid + pivot) % len(nums)
        if nums[mid_pivot] > target:
            right = mid - 1
        elif nums[mid_pivot] < target:
            left = mid + 1
        else:
            return mid_pivot

    return -1


# 정렬되어있긴 한데, 피벗을 기준으로 입력값이 돌아간 상황
#  정렬된 입력값은 [0,1,2,4,5,6] 에서 인덱스 + 피벗
print(solution_pivot([4, 5, 6, 7, 0, 1, 2], 1))
