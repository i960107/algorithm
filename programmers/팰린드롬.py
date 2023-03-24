# 부분 문자열 중 가장 긴 팰린드롬의 길이
def solution(s: str) -> int:
    def is_palindrome(start: int, end: int) -> bool:
        for index in range(start, (start + end) // 2 + 1):
            if s[index] != s[end - (index - start)]:
                return False
        return True

    start = end = 0
    answer = 0
    while start < len(s):
        if is_palindrome(start, end):
            length = (end - start + 1)
            if length > answer:
                answer = length
            # 두글자 늘려야할때도 있음
            end += 1
        else:
            start += 1
    return answer


print(solution("abcdcba"))
print(solution("a"))
print(solution("abacde"))
