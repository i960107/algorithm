from typing import List


def solution(word: str) -> int:
    sequence = 0
    order = ["A", "E", "I", "O", "U"]
    order_d = {
        "A": 0,
        "E": 1,
        "I": 2,
        "O": 3,
        "U": 4,
    }

    curr = []
    target = [char for char in word]

    found = False
    while not found:
        sequence += 1
        if len(curr) < 5:
            curr.append(order[0])
        else:
            index = len(curr) - 1
            while True:
                last_char_order = order_d[curr[index]]
                if last_char_order + 1 >= len(order):
                    curr.pop()
                    index -= 1
                else:
                    break
            curr[index] = order[order_d[curr[index]] + 1]
        print(curr)
        found = is_found(curr, target)

    return sequence


def is_found(arr: List[str], target: List[str]) -> bool:
    # 주의! zip은 대상들 중 가장 짧은 길이만큼만 반복함!
    if len(arr) != len(target):
        return False

    for a, b in zip(arr, target):
        if a != b:
            return False
    return True


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("UUUUU"))
