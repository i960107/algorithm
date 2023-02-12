from typing import List


#
# '''팰린드롬 게임 위너 구하기'''
#
#
# # 하나의 수 1만 뺄 수 있음
# # 정확성 테스트 실패.

# 모든 플레이어가 최적으로 play한다는 건,
# 그리디로 가장 빠르게 팰린드롬이 되는 경로를 선택한다 X.
# dfs로 모든 경로를 탐색해서 한번이라도 첫번째 플레이어가 이기는 경우가 있는지 체크해야함. 이길 가능성이 있는 경로를 선택한다.
# '최적으로'라는 단어에 끌려서 그리디의 최적 부분 구조를 떠올림..

def solution_dfs(queries: List[List[int]]) -> List[int]:
    answer = []
    for query in queries:
        winner_turns = dfs(query)
        answer.append(int(can_first_player_win(winner_turns)))
    return answer


def can_first_player_win(winner_turns: List[int]) -> bool:
    for winner_turn in winner_turns:
        if winner_turn % 2 == 1:
            return True
    return False


def dfs(query: List[int]) -> List[int]:
    stack = []
    stack.append((query, 0))
    visited = set()

    winner_turns = []
    while stack:
        query, turn = stack.pop()
        path = ''.join(str(num) for num in query)
        if path in visited:
            continue
        visited.add(path)

        if is_palindrome(query):
            winner_turns.append(turn)

        next_turn = turn + 1
        for index, num in enumerate(query):
            if num == 0:
                continue
            next_query = query.copy()
            next_query[index] -= 1
            stack.append((next_query, next_turn))

    return winner_turns


def is_palindrome(query: List[int]) -> bool:
    n = len(query)
    count = 0
    for index in range(n // 2):
        pair_index = n - 1 - index
        if query[index] != query[pair_index]:
            return False
    return True


def solution_greedy(queries: List[List[int]]) -> List[int]:
    answer = []
    for query in queries:
        winnable = False
        turn = get_required_count_to_make_palindrome(query)
        if turn % 2 == 1:
            answer.append(1)
            continue
        for index, x in enumerate(query):
            if x != 0:
                temp = query.copy()
                temp[index] = x - 1
                turn = get_required_count_to_make_palindrome(temp)
                turn -= 1
                player = 1 if turn % 2 == 1 else 2
                if player == 1:
                    winnable = True
                    break
        answer.append(int(winnable))
    return answer


def get_required_count_to_make_palindrome(query: List[int]) -> int:
    n = len(query)
    count = 0
    for index in range(n // 2):
        pair_index = n - 1 - index
        count += abs(query[index] - query[pair_index])
    return count


print(solution_greedy([[2, 0], [3, 1]]))
print(solution_greedy([[1, 4, 3], [1, 2, 2]]))
print(solution_greedy([[0, 2, 0, 1], [0, 1, 0, 1]]))
print(solution_greedy([[0, 9], [1, 9, 8, 0]]))
print(solution_greedy([[1, 9, 8, 0, 1]]))
print(solution_greedy([[1, 1, 3], [9, 0, 0], [1, 0, 2, 4]]))

print()

print(solution_dfs([[2, 0], [3, 1]]))
print(solution_dfs([[1, 4, 3], [1, 2, 2]]))
print(solution_dfs([[0, 2, 0, 1], [0, 1, 0, 1]]))
print(solution_dfs([[0, 9], [1, 9, 8, 0]]))
print(solution_dfs([[1, 9, 8, 0, 1]]))
print(solution_dfs([[1, 1, 3], [9, 0, 0], [1, 0, 2, 4]]))
