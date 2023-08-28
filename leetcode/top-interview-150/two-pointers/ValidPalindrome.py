# 1. 앞에서 i번째 문자와 뒤에서 i번째 문자를 "쌍으로" 비교 -> two pointers
def solution(s: str):
    new_s = []
    for c in s:
        if c.isalpha():
            new_s.append(c.lower())
        elif c.isnumeric():
            new_s.append(c)

    for i in range(len(new_s) // 2):
        left, right = new_s[i], new_s[-i - 1]
        if left != right:
            return False
    return True


def solution2(s: str):
    start = 0
    end = len(s) - 1  # 마지막 인덱스

    while start < end:
        # 1. start 인덱스를 증가시키며 숫자 또는 영문자를 찾는다. 인덱스가 len(s)보다 커지지 않도록 한다.
        # index out of range 예외가 발생하기 쉽고
        # .,와 같이 특수문자만 이루어진 경우에 처리하기가 쉽지 않음.
        # 한번 문자열 조작을 한 후에 순회하는것이 좋음.
        while not s[start].isalnum() and start < len(s):
            start += 1

        # 1. 인덱스를 감소시키며 숫자 또는 영문자를 찾는다. 인덱스가 0보다 작아지지 않도록 한다.
        while not s[end].isalnum() and end > 0:
            end -= 1

        if start > end:
            return False

        if s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1
    return True


def solution3(s: str):
    s = [c.lower for c in s if c.isalnum()]

    for i in range(len(s) // 2):
        left, right = s[i], s[~i]
        if left != right:
            return False
    return True
