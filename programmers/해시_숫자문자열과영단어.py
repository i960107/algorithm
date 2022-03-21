def solution(s: str) -> int:
    d = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    # 숫자를 문자로 취급해야지만 더할 수 있음. 아니면 덧셈이 됨
    answer = ""
    curr = ""
    # 선형 탐색해야하지만 길이가 배열 길이가 짧기 때문에 크게 성능 저하되지 않음
    l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for char in s:
        if char in l:
            answer += char
        else:
            curr += char
            # dict 형에서 없는 값을 조회하면? None
            if d.get(curr):
                answer += d.get(curr)
                curr = ""
    return int(answer)


def solution_others(s: str) -> str:
    d = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    answer = s
    for key, value in d.items():
        answer = answer.replace(key, value)
    return int(answer)


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
