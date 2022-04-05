import bisect
from typing import List


def solution(g: List[int], s: List[int]) -> int:
    answer = 0
    g.sort()
    s.sort()
    i, j = 0, 0
    # 만족하지 못할때까지 그리디 진행?
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            answer += 1
            i += 1
            j += 1
        elif s[j] < g[i]:
            j += 1

    return answer


def solution_bisect(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    result = 0
    for i in s:
        # 찾아낸 인덱스가 현재 부여한 아이들보다 크다면 더 줄 수 있다는 말?
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1
    return result


print(solution(g=[1, 2, 3], s=[1, 1]))
print(solution(g=[1, 2], s=[1, 2, 3]))

str.isal