def solution_bracket(p: str) -> str:
    left = "("
    right = ")"
    d = {left: right, right: left}

    def is_valid_bracket(s: str) -> bool:
        # 올바른 괄호인지
        stack = []
        for side in s:
            if side == left:
                stack.append(side)
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        return not stack

    def is_balanced_bracket(s: str) -> bool:
        l, r = 0, 0
        for side in s:
            if side == left:
                l += 1
            else:
                r += 1
        return l == r

    def validate_bracket(s: str) -> str:
        # u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야하며(앞에서부터 균형 잡힌 문자열 중 최소)
        # v는 빈 문자열이 될 수 있음

        i = 0
        u = s[i:i + 2]
        while not is_balanced_bracket(u):
            i += 2
            u += s[i:i + 2]
        v = s[i + 2:]

        # u가 올바른 문자열일때
        if is_valid_bracket(u):
            # 재귀 호출이 종결되는 곳
            if is_valid_bracket(v):
                return u + v
            else:
                v = validate_bracket(v)
                return u + v
        # u가 올바른 문자열이 아닐때
        else:
            v = '(' + validate_bracket(v) + ')'
            u = ''.join(d.get(side) for side in u[1:-1])
            return v + u

    # 빈 문자열이거나 올바른 괄호 문자열이라면
    if not p or is_valid_bracket(p):
        return p
    else:
        return validate_bracket(p)


# 올바른 문자열
print(solution_bracket("(()())()"))
# 빈 문자열
print(solution_bracket(""))

print(solution_bracket(")("))
print(solution_bracket("()))((()"))
