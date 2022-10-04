def solution(s: str) -> int:
    min_length = len(s)

    for u in range(1, len(s) // 2 + 1):

        curr_length = 0

        prev = ""
        cnt = 0

        test = ""

        i = 0

        while i < len(s):
            curr = s[i:i + u]
            # 마지막에 추가되지 않은 글자들 있음.
            if curr == prev:
                cnt += 1

            else:
                test += str(cnt) + prev if cnt > 1 else prev
                curr_length += (u + 1 if cnt > 1 else u)
                prev = curr
                cnt = 1

            i += u

        test += str(cnt) + prev if cnt > 1 else prev
        test += s[i:]

        # curr_length += u + 1 if cnt > 1 else u
        # curr_length += (len(s) % u)
 # curr_length += (len(s) - i)

        print("정답", len(test), "오답", curr_length)
        min_length = min(len(test), min_length)

    return min_length


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))

