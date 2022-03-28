def solution_valid_bracket(s: str) -> bool:
    left = "("
    right = ")"
    stack = []
    for side in s:
        if side == left:
            stack.append(side)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return not stack


print(solution_valid_bracket("()()"))
print(solution_valid_bracket("(())()"))
print(solution_valid_bracket(")()("))
print(solution_valid_bracket("(()("))
