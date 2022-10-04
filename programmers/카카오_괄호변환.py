def get_valid_bracket_str(p: str) -> str:
    if not p:
        return p

    i = 0
    left = right = 0

    while left == 0 or left != right:
        if p[i] == "(":
            left += 1
        else:
            right += 1
        i += 1

    u, v = p[:i], p[i:]

    # print("u", u, "v", v)

    def is_balanced_bracket_str(s: str) -> bool:
        answer = 0
        for bracket in s:
            if bracket == "(":
                answer += 1
            else:
                answer -= 1
            if answer < 0:
                return False

        return answer == 0

    if is_balanced_bracket_str(u):
        return u + get_valid_bracket_str(v)
    else:
        return "(" + get_valid_bracket_str(v) + ")" + \
               "".join(["(" if bracket == ")" else ")" for bracket in u[1:-1]])


print(get_valid_bracket_str("(()())()"))
print(get_valid_bracket_str(")("))
print(get_valid_bracket_str("()))((()"))
