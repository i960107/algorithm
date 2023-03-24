from typing import List, Deque
from collections import deque


# 단서를 빠뜨림 -> 서로 다른 단어만 존재
# def solution(cards1: List[str], cards2: List[str], goal: List[str]) -> str:
#     # 2개로 dfs하는 법..
#     # cards1과 cards2가 같을때, 어떤 걸 쓰느냐에 따라 달라질 수 있음..
#     # dfs로 해볼까? 모든 경우를 살펴야함..
#
#     # deque(에서 빼볼까?)
#     cards1 = deque(cards1)
#     cards2 = deque(cards2)
#     goal = deque(goal)
#
#     def dfs(cards1: Deque[str], cards2, words: int, path):
#         # index가 가리키는 것은 포함된 마지막 단어의 인덱 + 1.?
#         # 번째 -> index -1
#         # index가 가리키는 것은 탐색범위의 시작 인덱스
#         # cards1 cards2 중에 어떤 걸 더해주ㅓ야할까..
#
#         if path == goal:
#             return True
#
#         result = False
#         if cards and cards1[0] == goal[words]:
#             popped_card = cards1.popleft()
#             path.append(popped_card)
#             if dfs(cards1, cards2, words + 1, path):
#                 result = True
#             path.pop()
#             cards1.appendleft(popped_card)
#
#         if not result and cards2[0] == goal[words]:
#             popped_card = cards2.popleft()
#             path.append(popped_card)
#             if dfs(cards1, cards2, words + 1, path):
#                 result = True
#             path.pop()
#             cards2.appendleft(popped_card)
#         return result
#
#     path = []
#     result = dfs(cards1, cards2, 0, path)
#     return "YES" if result else "NO"
#
#
def solution(cards1: List[str], cards2: List[str], goal: List[str]) -> str:
    # 아직 포함되지 않은 단어
    index1 = 0
    index2 = 0
    goal_index = 0
    while goal_index < len(goal):

        if index1 == len(cards1) and index2 == len(cards2):
            break

        found = False
        if index1 < len(cards1) and cards1[index1] == goal[goal_index]:
            print(cards1[index1])
            index1 += 1
            goal_index += 1
            found = True

        if index2 < len(cards2) and cards2[index2] == goal[goal_index]:
            print(cards2[index2])
            index2 += 1
            goal_index += 1
            found = True

        if not found:
            break

    print(goal_index)
    return "YES" if goal_index == len(goal) else "NO"


def solution2(cards1: List[str], cards2: List[str], goal: List[str]) -> str:
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for word in goal:
        if cards1 and cards1[0] == word:
            cards1.popleft()
            continue
        elif cards2 and cards2[0] == word:
            cards2.popleft()
            continue
        else:
            return "No"
    return "Yes"


print(solution2(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution2(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
