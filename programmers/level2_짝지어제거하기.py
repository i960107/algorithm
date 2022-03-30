def solution(s: str) -> int:
    stack = []
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()

    return int(not stack)


print(solution("baabaa"))
print(solution("cdcd"))
