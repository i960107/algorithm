def solution(n: int, goorm_numbers: str) -> int:
    d = {
        "qw": "1",
        "as": "2",
        "zx": "3",
        "we": "4",
        "sd": "5",
        "xc": "6",
        "er": "7",
        "df": "8",
        "cv": "9",
        "ze": "0",
    }

    i = 0
    answer = []
    while i < n - 1:
        curr = goorm_numbers[i:i + 2]
        if curr in d:
            answer.append(d[curr])
        i += 1

    return int(''.join(answer))

    pass


print(solution(4, "qwer"))
print(solution(10, "sdweasweas"))
