def solution(d: list, budget: int) -> int:
    d.sort()
    # 0개 기업만 지원 가능할떼!!
    if d[0] > budget:
        return 0
    left = 0  # 1개 기업만 지원
    right = len(d) - 1  # 전체 기업 지원
    while left + 1 < right:
        mid = (left + right) // 2
        if budget >= sum(d[:mid + 1]):
            left = mid
        else:
            right = mid
    return left + 1 if budget < sum(d[:right + 1]) else right + 1


def solution_others(d: list, budget: int) -> int:
    d.sort()
    accumulated = sum(d)
    # 0개 기업만 지원 가능할때 어떻게 처리되지?
    # 지원 기업 0개일때 필요 금액 = 0 >= budget 이게 되어있음.
    while budget < accumulated:
        accumulated -= d.pop()
    return len(d)


print(solution([1, 3, 2, 5, 4], 9))
print(solution([1, 3, 2, 5, 4], 1))
print(solution([1, 3, 2, 5, 4], 0))
print(solution([2, 2, 3, 3], 10))

# print(solution_others([1, 3, 2, 5, 4], 9))
# print(solution_others([1, 3, 2, 5, 4], 1))
print(solution_others([3, 3, 2, 5, 4], 2))
# print(solution_others([2, 2, 3, 3], 10))

# 탈출 조건 lo <= hi, lo< hi, lo +1 < hi,
# 정답이 lo인지 hi인지 mi인지
# 많은 최적화문제의 경우  이분탐색으로 풀 수 있음 Check(x)를 만족하는 x의 최댓값 또는 최솟값. check(x)가 x에 대해 이분적이면 이분 탐색 가능
# lo +1 < hi인 동안(lo < mid <hi) check(lo) == check(mid)라면 lo= mid, check(hi) == check(mid)라면 hi == mid를 해주기.
# 반복문을 탈출했다면 lo +1 >= hi 즉 lo + 1 == hi인 경우임
# 가장 큰 F라면 lo를 가장 작은 T라면 hi를 출력
'''1~50까지 오룸차순 정렬된 카드에서 28번 카드를 찾는 문제'''


# check 조건은 x >= num
def solution_binary_search(l: list, num: int) -> int:
    lo = 0  # check[lo] = False
    hi = len(l) - 1  # check[hi] = True
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if l[mid] >= num:  # check[mid] == check[upper]
            hi = mid
        else:
            lo = mid
    # 몇 번째 수인지
    return hi + 1 if l[hi] == num else -1


print(solution_binary_search([i for i in range(1, 51)], 28))
print(solution_binary_search([i for i in range(1, 51)], 50))
print(solution_binary_search([i for i in range(1, 51)], 0))


def solution_upper_bound(l: list, num: int) -> int:
    '''l[i] > num 인 i의 최소값(l[i-1]<k<=l[i], 이상)'''
    left, right = 0, len(l)
    while left < right:  # left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = (left + right) // 2
        # mid = left + (right - left) // 2 같음
        if l[mid] < num:
            left = mid + 1
        else:
            right = mid
    return right + 1 if l[right] == num else -1


def solution_lower_bound(l: list, num: int) -> int:
    '''l[i] >= num 인 i의 최소값(l[i-1]<=k<l[i], 초과)'''
    left, right = 0, len(l)
    while left < right:  # left와 right가 만나는 지점이 target 초과 값이 처음 나오는 위치
        mid = left + (right - left) // 2
        if l[mid] < num:
            left = mid + 1
        else:
            right = mid
    return right + 1 if l[right] == num else -1


print(solution_upper_bound([i for i in range(1, 51)], 28))
print(solution_upper_bound([i for i in range(1, 51)], 50))
print(solution_upper_bound([i for i in range(1, 51)], 0))
print(solution_lower_bound([i for i in range(1, 51)], 28))
print(solution_lower_bound([i for i in range(1, 51)], 50))
print(solution_lower_bound([i for i in range(1, 51)], 0))
