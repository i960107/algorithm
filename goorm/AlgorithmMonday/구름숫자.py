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


def solution(n: int, goorm_numbers: str) -> int:
    answer = []
    for i in range(len(goorm_numbers) - 1):
        curr = goorm_numbers[i:i + 2]
        if curr in d:
            answer.append(d[curr])
    return int(''.join(answer))


n = int(input())
goorm_numbers = input()
print(solution(n, goorm_numbers))
