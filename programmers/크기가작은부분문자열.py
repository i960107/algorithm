def solution(t: str, p: str) -> int:
    P = len(p)
    p = int(p)
    count = 0
    for start in range(len(t) - P + 1):
        part_t = int(t[start: start + P])
        if  part_t <= p:
            count += 1
    return count


# 왜 실패했지?
def solution_fail(t: str, p: str) -> int:
    count = 0

    if len(p) == 1:
        return sum([1 for x in t if x <= p])

    for start in range(len(t) - len(p) + 1):
        is_smaller_or_equal = False
        # 한자리인 경우,
        for index, num in enumerate(p):
            if t[start + index] < num:
                is_smaller_or_equal = True
                break

            if t[start + index] > num:
                is_smaller_or_equal = False
                break

        if is_smaller_or_equal:
            count += 1

    return count


print(solution("3141592", "271"))
print(solution("50022083978", "7"))
print(solution("502217", "22"))
