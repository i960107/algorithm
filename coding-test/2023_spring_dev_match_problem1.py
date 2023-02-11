from typing import List
'''구입할 복권 구하기'''

def solution(lotteries: List[List[int]]) -> int:
    analyzed = []
    for index, (winners, buyers, prize) in enumerate(lotteries):
        analyzed.append((-(winners / (buyers + 1)) if winners < buyers + 1 else -1, -prize, index + 1))
    analyzed.sort()
    print(analyzed)

    return analyzed[0][2]


# 당첨확률이 높은 순, 당첨 금액이 높은 순, winner, buyers, prize 내가 사지 않은 상태
print(solution([[100, 100, 500], [1000, 1000, 100]]))
print(solution([[10, 19, 800], [20, 39, 200], [100, 199, 500]]))
print(solution([[50, 1, 50], [100, 199, 100], [1, 1, 500]]))
