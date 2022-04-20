from typing import List


# if the serach ends with an empty half, the condition cannot be fulfuilled and target is not found
# the condition is unsatisfied or values unequal
# the half in which the target cannot lie is eliminated
# how to idnetify binary search problems -> 탐색 범위를 2개로 나누어서 줄여간다.
# why we use binary search -> 선형 검색보다 빠르다. 매번 탐색해야할 때마다 정렬후 이진검색이 더 나은 옵션인지 고려해보기
# search for a specific value
# apply search condition

def template1(nums: List[int], target: int) -> int:
    ''''Most Basic: search space is determined by accessing a single index in the array'''
    if not nums:
        return -1
    l, u = 0, len(nums)
    while l <= u:
        mid = l + (u - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            u = mid - 1
    # no post-processing required, because every time you check if the element has been found
    # end condition: left > right
    return -1


def template1_sqrt(x=4) -> int:
    # n*n <=4가 되는 largest value
    l, u = 0, x
    while l <= u:
        mid = (l + u) // 2
        if mid * mid < x:
            l = mid + 1
        elif mid * mid > x:
            u = mid - 1
        else:
            # mid가 정답이 되는 조건 mid * mid = x일때 혹은  mid * mid <= x < (mid+1) * (mid +1)
            return mid
    # l > u일때 빠져나옴
    return u


def template1_sqrt_others(x=4) -> int:
    # condition을 정확히 표현하기.
    if x == 0:
        return 0
    # 왜 1부터 시작할까?
    # zero division error 방지 위해 0은 예외 처리
    l, u = 1, x
    while l <= u:
        mid = l + (u - l) // 2
        # stack overflow 방지
        if mid <= x / mid and x / (mid + 1) < (mid + 1):
            return mid
        elif mid <= x / mid:
            l = mid + 1
        else:
            u = mid - 1


def template1_search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
    pivot = 0
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            pivot = i

    l, u = 0, len(nums) - 1
    while l <= u:
        mid = l + (u - l) // 2
        pivoted_mid = (mid + pivot) % len(nums)
        if nums[pivoted_mid] < target:
            l = mid + 1
        elif nums[pivoted_mid] > target:
            u = mid - 1
        else:
            return pivoted_mid
    return -1


def template1_search_in_rotated_sorted_array_others(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    # 최소값을 찾아 피벗 설정
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            right = mid
    # l = r 일때 순환문 빠져나옴
    pivot = l

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        mid_pivot = (mid + pivot) % len(nums)

        if nums[mid_pivot] < target:
            l = mid + 1
        elif nums[mid_pivot] > target:
            r = mid - 1
        else:
            return mid_pivot
    return -1


# print(template1_search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0))
# print(template1_search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3))
# print(template1_search_in_rotated_sorted_array([1], 0))

# modulo operation on negative number
# return a number having the same sign as the denominator
# (-1 * 7 + 6) % 7 => ((7-1) % 7과 같음)
# print(-1 % 7)  # 6

def template2(nums, target):
    '''accessing the current index and its immediate right neighbor in the array'''
    # 최소 길이가 2이상이어야함
    if len(nums) == 0:
        return -1
    # len(nums) -1 아니고 len(nums)임
    l, u = 0, len(nums)
    while l < u:
        mid = l + (u - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            u = mid

    # post-processing
    # template1 no elemenst left all elements are checked
    # end condition: left == right. one elements left. check if the element meets the condition
    # l == len(nums)인 경우 있나? 초기 search space가 len(n) 포함
    if l != len(nums) and nums[l] == target:
        return l
    return -1


def template2_first_bad_version(n: int, bad: int) -> int:
    # 이건 template1으로 풀 수 없나?
    # BadVersion인 것들 중 최솟값
    def isBadVersion(version: int) -> bool:
        if version >= bad:
            return True
        return False

    l, u = 1, n

    while l < u:
        mid = l + (u - l) // 2
        # mid가 badversion 중 최솟값일 수 있음
        if isBadVersion(mid):
            u = mid
        else:
            # 컨디션 만족하지 않으므로 다음 번에 mid +1 부터 탐색
            l = mid + 1

    # l == u 일때 나옴
    return l


def template1_first_bad_version(n: int, bad: int) -> int:
    def isBadVersion(version: int) -> bool:
        if version >= bad:
            return True
        return False

    l, u = 1, n - 1
    while l <= u:
        mid = l + (u - l) // 2
        if isBadVersion(mid):
            u = mid - 1
        else:
            l = mid + 1

    # 흠 이게 맞나
    return u + 1


def template1_find_peak_elements(nums: List[int]) -> int:
    l, u = 0, len(nums) - 1
    while l < u:
        # l, mid는  len(nums)-2이 될 수 있음. 따라서 list index out of range error 발생하지 않음
        mid = l + (l - u) // 2
        # the peak will always lie towards teh left of this elements(inclusive)
        if nums[mid] > nums[mid + 1]:
            u = mid
        else:
            l = mid + 1

    # l == u 이기 때문에 return u도 가
    return l


def template2_find_minimum_in_rotated_sorted_array(num: List[int]) -> int:
    '''내풀이'''
    # right가 아니라 left를 봐야되는 것 아닌가
    # 어떤 값을 찾아야할까 condition이 뭘까. num[mid-1] > num[mid] 인 값 하나를 찾는다?
    if len(num) == 0:
        return -1
    l, u = 0, len(num) - 1

    while l < u:
        mid = l + (u - l) // 2
        # 왜 right와 비교하는거지?
        if num[mid] < num[u]:
            u = mid
        # 꼭  u=  mid+1은 아님!. 탐색대상은 mid의 오른쪽이 되어야 함
        else:
            l = mid + 1

    # l == u 일때 즉 한 원소 남음.
    return num[u]


def template2_findMin(nums: List[int]) -> int:
    '''leetcode풀이'''
    # 빈배열일때는?
    if not nums:
        return -1

    if len(nums) == 1:
        return nums[0]

    l, r = 0, len(nums) - 1
    # ascending하는 배열일때. 즉 not rotated면 first element < last elements
    # no rotation
    if nums[r] > nums[0]:
        return nums[0]

    # find inflection point(변곡점). left element > right element
    # all the elements to the left of inflection point> first element of the array
    # all the elements to the right of inflection point< first element of the array
    while l <= r:
        mid = l + (r - l) // 2
        # inflection point인지 찾기.
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # inflection point아니므로 mid제외
        if nums[mid] > nums[0]:
            l = mid + 1
        else:
            u = mid - 1


# print(template2_findMin([]))
# print(template2_findMin([3, 4, 5, 1, 2]))
# print(template2_findMin([4, 5, 6, 7, 0, 1, 2]))
# print(template2_findMin([11, 13, 15, 17]))
# print(template2_findMin([11, 13, 15, 17]))
#
# print(template2_findMin([2, 1]), "테스트")


def template2_find_minimum_in_rotated_sorted_array_others(num: List[int]) -> int:
    # all the elements to the left of mid > first element of array. right < first elements of the array
    if not num:
        return -1

    if num[0] <= num[-1]:
        return num[0]
    l, u = 0, len(num) - 1
    while l < u:
        mid = l + (u - l) // 2
        # if num[mid] > num[0]:안됨
        if num[mid] >= num[0]:
            l = mid + 1
        else:
            u = mid
    return num[l]


# print(template2_find_minimum_in_rotated_sorted_array_others([2, 1]), "테스트")
# print(template2_find_minimum_in_rotated_sorted_array([]))
# print(template2_find_minimum_in_rotated_sorted_array([3, 4, 5, 1, 2]))
# print(template2_find_minimum_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2]))
# print(template2_find_minimum_in_rotated_sorted_array([11, 13, 15, 17]))
# # ascending value만 있을때 에러 남!
# print(template2_find_minimum_in_rotated_sorted_array_others([11, 13, 15, 17]))


def template3(nums, target):
    '''accessing the current index and its immediate left and right neighbor in the array'''
    if len(nums) == 0:
        return -1
    l, u = 0, len(nums) - 1
    # search space is at least 3 in size at each step
    while l + 1 < u:
        mid = l + (u - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid
        else:
            u = mid

    # post- processing
    # end condition : l + 1 == u. two elements left
    if nums[l] == target: return l
    if nums[u] == target: return u
    return -1


def template3_search_for_a_range(nums: List[int], target: int) -> List[int]:
    # bisect left, bisect right한 결과를 찾아야되는 구만
    answer = [-1, -1]

    if not nums:
        return answer

    # nums[i] == target인 i중 가장 작은것, 가장 큰것
    l, u = 0, len(nums) - 1

    # 일단 일치하는 원소 찾아서 왼쪽으로 진행
    # bisect left?
    while l <= u:
        mid = l + (u - l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            u = mid - 1
        else:
            answer[0] = mid
            u = mid - 1

    l, u = 0, len(nums) - 1
    # bisect right?
    while l <= u:
        mid = l + (u - l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            u = mid - 1
        else:
            answer[1] = mid
            l = mid + 1

    return answer


print(template3_search_for_a_range(nums=[5, 7, 7, 8, 8, 10], target=8))
print(template3_search_for_a_range(nums=[5, 7, 7, 8, 8, 10], target=6))
print(template3_search_for_a_range(nums=[], target=0))


def template3_find_k_cloest_element(arr: List[int], k: int, x: int) -> List[int]:
    answer = []
    # l, u = 0, len(arr) - 1
    # index = -1
    # while l <= u:
    #     mid = l + (u - l) // 2
    #     if arr[mid] > x:
    #         u = mid - 1
    #     elif arr[mid] < x:
    #         l = mid + 1
    #     else:
    #         index = mid
    #         break
    #
    # p1, p2 = index, index
    # print(p1, p2)
    #
    # while k > 0 and p1 >= 0 and p2 < len(arr):
    #     if arr[p1] - x <= x - arr[p2]:
    #         answer.append(arr[p1])
    #         p1 -= 1
    #     else:
    #         answer.append(arr[p2])
    #         p2 += 1
    #     k -= 1
    return answer[::-1]


print(template3_find_k_cloest_element(arr=[1, 2, 3, 4, 5], k=4, x=3))
# x가 arr안에 없을 수도 있음!
print(template3_find_k_cloest_element(arr=[1, 2, 3, 4, 5], k=4, x=-1))
