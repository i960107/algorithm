from collections import defaultdict
from math import sqrt


def solution(left: int, right: int) -> int:
    # 약수의 개수는 어떻게 구하는 거지? 약수가 홀수개인 모든 수는 제곱수!

    # arr[0] = left 약수의 개수
    arr = [1 for _ in range(left, right + 1)]

    # O(n^2)
    for i in range(2, right + 1):
        for j in range(left, right + 1):
            if j % i == 0:
                arr[j - left] += 1

    return sum(i + left if cnt % 2 == 0 else -(left + i) for i, cnt in enumerate(arr))


def solution_others(left: int, right: int) -> int:
    # 수의 특징을 활용해야 하는 문제라면 검색해보기!

    answer = 0
    # O(N)
    for num in range(left, right + 1):
        # 제곱근 구하기 i**0.5
        if int(sqrt(num)) == sqrt(num):
            answer -= num
        else:
            answer += num
    return answer


print(solution(13, 17))
print(solution(24, 27))
