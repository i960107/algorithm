from typing import List
from itertools import product


def solution_fail(num: str) -> List[str]:
    d = {
        "2": ["A", "B", "C"],
        "3": ["D", "E", "F"],
        "4": ["G", "H", "I"],
        "5": ["J", "K", "L"],
        "6": ["M", "N", "O"],
        "7": ["P", "Q", "R", "S"],
        "8": ["T", "U", "V"],
        "9": ["W", "X", "Y", "Z"],
    }
    answer = []
    for n in num:
        # 배열에 배열 곱한다고 cartesian곱 되지 않음,.
        # can't multiply sequence
        answer *= d[n]
    return answer


def solution2(digits: str) -> List[str]:
    # index는 digits에서 몇번째 값을 탐색할지를 뜻함
    def dfs(index: int, path: str):
        # 끝까지 탐색하면 백트래킹
        if index == len(digits):
            # if len(path) == len(digits):
            # hoisting 때문에 result참조가능
            result.append(path)
            return

        # 입력값 자릿수 단위 반복. 입력값을 자릿수로 쪼개어 반복?
        # 불필요한 탐색 일어남. 첫번째 자리에 올 수 있는 숫자는 index에 해당하는 문자뿐임
        # for i in range(index, len(digits)):
        #     for j in dic[digits[i]]:
        #         dfs(i + 1, path + j)

        for d in dic[digits[index]]:
            dfs(index + 1, path + d)

    dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    # 입력값 자리수 반복
    if not digits:
        return []

    result = []
    dfs(0, "")

    return result


def solution_mine(digits: str) -> List[str]:
    answer = []
    dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def dfs(index: int, path):
        if index == len(digits):
            answer.append(''.join(path))
            return
        chars = dic[digits[index]]
        for char in chars:
            path.append(char)
            dfs(index + 1, path)
            path.pop()

    if not digits:
        return answer
    dfs(0, [])

    return answer


def letterCombination(digits: str) -> List[str]:
    dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    if not digits:
        return []
    result = []

    def dfs(index: int, path: List[str]):
        # 왜 여기 못 넘어가지?
        # index는 다음 추가할 인덱스를 말하는 것으로! index = len(digits)일때 완성된 형태
        if not (0 <= index <= len(digits)):
            return

        if len(path) == len(digits):
            result.append("".join(path))
            return
        for char in dic[digits[index]]:
            dfs(index + 1, path + [char])

    dfs(0, [])
    return result


print(solution2("23"))
print(solution2("234"))
print(solution2("345629"))
