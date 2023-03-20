from typing import List
from collections import defaultdict


def solution(keymap: List[str], targets: List[str]) -> List[int]:
    key_dict = defaultdict(int)

    for keyboard in keymap:
        for count, char in enumerate(keyboard, 1):
            if char not in key_dict or key_dict[char] > count:
                key_dict[char] = count

    answer = []
    for target in targets:
        possible = True
        count = 0
        for char in target:
            if char not in key_dict:
                possible = False
                break
            count += key_dict[char]
        if not possible:
            answer.append(-1)
        else:
            answer.append(count)
    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
print(solution(["AA"], ["B"]))
