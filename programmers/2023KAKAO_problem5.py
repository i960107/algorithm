from typing import List


def solution(commands: List[str]) -> List[str]:
    table = [[None] * 51 for _ in range(51)]

    answer = []
    merged = dict()

    def update(r: int, c: int, value: str):
        table[r][c] = value

    def update_values(value1: str, value2: str):
        for r in range(1, 51):
            for c in range(1, 51):
                if table[r][c] == value1:
                    table[r][c] = value2

    def merge(r1: int, c1: int, r2: int, c2: int):
        print("merge")


    def unmerge(r: int, c: int):
        print("unmerge")

    def _print(r: int, c: int):
        print("print")
        answer.append(table[r][c])

    for command in commands:
        action = command.split()[0]
        target = command.split()[1:]

        if action == "UPDATE":
            if len(target) == 2:
                update_values(*target)
            else:
                update(int(target[0]), int(target[1]), target[2])

        if action == "PRINT":
            _print(*map(int, target))
        if action == "MERGE":
            merge(*map(int, target))
        if action == "UNMERGE":
            unmerge(*map(int, target))

    return answer


print(solution([
    "UPDATE 1 1 menu",
    "UPDATE menu menu2",
    "PRINT 1 1",
    "MERGE 1 1 1 2",
    "UNMERGE 1 2",
]))
