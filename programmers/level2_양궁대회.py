from typing import List


def solution(n: int, info: List[int]) -> List[int]:
    memo = [[0] * (n + 1) for _ in range(11)]

    # for i, x in enumerate(info):
    #     # required 발을 맞춰야 점수 score를 얻는지
    #     required, score = x + 1, 10 - i
    #     # 현재 과녁을 맞춰서 점수를 얻는 경우, 현재 과녁을 맞추지 않고 이전 과녁까지 얻은 최대 점수를 비교
    #     max(memo[i-1][n - required] + score, memo[i-1][n])

    for total_cost in range(1, n + 1):
        if info[0] + 1 <= total_cost:
            memo[0][total_cost] = 10

    # 정확히 total_cost만큼 써서 과녁 0..last_index까지의 과녁을 맞춰서 얻을 수 있는 최대 점수
    for last_index in range(1, 11):
        for total_cost in range(1, n + 1):
            # last_index의 과녁을 맞춰 score의 점수를 얻기 위해서 required발을 맞춰야함
            required, score = info[last_index] + 1, 10 - last_index
            if required > total_cost:
                memo[last_index][total_cost] = memo[last_index - 1][total_cost]
            else:
                memo[last_index][total_cost] = max(memo[last_index - 1][total_cost],
                                                   (memo[last_index - 1][total_cost - required] + score))

    for i in range(11):
        print(10 - i, memo[i])

    scores = []
    for i in range(11):
        if memo[i -1][n] == memo[i][n]:
            score
        else:
            scores.append([i])

    return memo[10][n]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))


# print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
# print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))

def get_winner(arr1, arr2) -> int:
    score1 = []
    score2 = []

    for i, x, y in zip(range(11), arr1, arr2):
        if x >= y:
            score1.append((10 - i))
        else:
            score2.append((10 - i))

    print(score1, score2)
    return 1 if sum(score1) >= sum(score2) else 2


print(get_winner([2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 1, 1, 1, 0, 0, 0, 0]))
