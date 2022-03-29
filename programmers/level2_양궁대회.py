from typing import List


def solution(n: int, info: List[int]) -> List[int]:
    answer = [0] * 11
    for i, count in enumerate(info):
        if n == 0:
            break
        answer[i] = count + 1
        n -= (count + 1)
    # 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러가지일 경우,
    # 가장 낮은 점수를 더 많이 맞힌 경우를 return

    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
