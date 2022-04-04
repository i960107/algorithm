from typing import List


def solution(prices: List[int]) -> int:
    answer = 0

    # 오를거면 일단사고 바로 팔아 또 오를거면 또 사 팔아 그러면 계속 가지고 있다가 정점에 파는거랑 같잖아!
    for i in range(1, len(prices)):
        if prices[i - 1] < prices[i]:
            answer += prices[i] - prices[i - 1]
    return answer


def solution_others(prices: List[int]) -> int:
    answer = 0
    # 내리기 전에 팔고 오르기 전에 산다
    # 계속 오르는 경우라도 몇 번이든 사고팔 수 있기 때문에, 매번 단계마다 이익을 취하는 탐용 구조로 구현할 수 있음
    return answer


print(solution([7, 1, 5, 3, 6, 4]))
print(solution([1, 2, 3, 4, 5]))
print(solution([7, 6, 4, 3, 1]))
