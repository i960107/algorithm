def solution(x: int, y: int, n: int) -> int:
    # index i는 10 + i를 만들기 위한 최소 연산횟수?
    # 마지막 인덱스는 y를 만들기 위한 최소 연산횟수
    # dp? 혹은 greedy?
    # 최대 1,000,000만이기 때문에 최대값 int(1e9)가능
    INF = int(1e9)
    min_operation = [INF] * (y - x + 1)
    min_operation[0] = 0
    for i in range(len(min_operation)):
        num = x + i

        # if num * 2 - x < len(min_operation):
        #     min_operation[num * 2 - x] = min(min_operation[i] + 1, min_operation[num * 2 - x])
        #
        # if num * 3 - x < len(min_operation):
        #     min_operation[num * 3 - x] = min(min_operation[i] + 1, min_operation[num * 3 - x])
        #
        # if num + n - x < len(min_operation):
        #     min_operation[num + n - x] = min(min_operation[i] + 1, min_operation[num + n - x])
        for nxt in (num * 2 - x, num * 3 - x, num + n - x):
            if nxt < len(min_operation):
                min_operation[nxt] = min(min_operation[i] + 1, min_operation[nxt])

    return min_operation[y - x] if min_operation[y - x] != INF else - 1


print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))
