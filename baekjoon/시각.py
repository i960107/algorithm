def solution(N: int) -> int:
    res = 0

    for h in range(N + 1):

        if h in [3, 13, 23]:
            res += 3600
        else:
            res += (45 * 15 + 15 * 60)

    return res


res = solution(5)
print(res, res == 11475)
