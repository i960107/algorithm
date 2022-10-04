from collections import deque


def solution(N: int) -> int:
    cards = deque([i for i in range(1, N + 1)])

    while len(cards) > 1:
        cards.popleft()
        cards.rotate(-1)

    return cards[0]


res = solution(6)
print(res, res == 4)
