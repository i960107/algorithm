from itertools import combinations


def solution_fail(n: int) -> int:
    case = 0
    for x in range(n + 1):
        if 2 * x > n:
            break
        y = n - (2 * x)
        # x =2 y =1 일때 case는 3가지. but 1가지만 추가됨
        # 2 2개 1 1개를 배열하는 경우의 수를 어떻게 코드로 구현하지? 완전히 중복 순열은 아님. 모듈 이용 없이 직접 구현해야함
        case += len(list(combinations([i for i in range(1, y + 2)], x)))
    return case % 10007


def solution_dp_tabulation(n: int) -> int:
    '''dynamic programming - tabulation 풀이'''
    cache = [0] * (n + 1)
    cache[1] = 1
    cache[2] = 2
    i = 3
    # while not cache[n]:
    while i <= n:
        cache[i] = cache[i - 2] + cache[i - 1]
        i += 1

    return cache[n] % 10007


n = int(input())
cache = [0] * (n + 1)
cache[1] = 1
cache[2] = 2


def solution_dp_memoization(n: int) -> int:
    '''dynamic programming - memoization 풀이'''
    if cache[n]:
        return cache[n]
    # 100007 cache에 넣어줄때부터 해야하나?
    cache[n] = (solution_dp_memoization(n - 2) + solution_dp_memoization(n - 1)) % 10007
    return cache[n]


print(solution_dp_tabulation(n))
print(solution_dp_memoization(n))
