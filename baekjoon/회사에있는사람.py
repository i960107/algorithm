import sys
from typing import List


def solution():
    input = sys.stdin.readline

    # 삽입과 삭제가 빈번하게 일어나고, 동명이인이 없으며!! 순서 중요하지 않음!
    company = set()
    for _ in range(int(input())):
        person, action = input().split()
        if action == "enter":
            company.add(person)
        else:
            company.remove(person)

    for person in (sorted(company, reverse=True)):
        print(person)


def solution2(logs: List[str]) -> List[str]:
    entered = set()
    left = set()

    for x in logs:
        name, action = x.split()
        if action == "enter":
            entered.add(name)
        else:
            left.add(name)
    return sorted(list(entered - left), reverse=True)


res = solution2(["Baha enter", "Askar enter", "Baha leave", "Artem enter"])
print(res, res == ["Askar", "Artem"])
