from typing import List, Tuple


def coin_change(coins: List[int], change: int) -> List[Tuple[int, int]]:
    '''가장 작은 동적 개수로 거슬러주는 방법'''
    # 금액이 큰 동전을 최대한 사용하기
    answer = []
    while change > 0:
        coin = coins.pop()
        if coin <= change:
            count = change // coin
            answer.append((coin, count))
            change -= count * coin
    return answer


print(coin_change([10, 50, 100, 500], 160))
