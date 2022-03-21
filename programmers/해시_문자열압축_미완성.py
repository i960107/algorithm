def solution(s: str) -> int:
    # 이진 탐색?
    left = 0
    right = len(s)

    answer = 0
    while left < right:
        mid = (left + right) // 2
        # for i in range(len(s) - mid):
        #     #O(n^2)
        #     s.replace()
        # 해시를 쓰는게 나을까?



    return answer


print(solution("aabbacc"))
