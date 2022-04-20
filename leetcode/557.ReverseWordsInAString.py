def reverseWords(s: str) -> str:
    answer = ""
    curr = ""
    # time complexity O(N) space complexity O(N)
    for char in s:
        if char == " ":
            answer += curr[::-1]
            answer += char
            curr = ""
        else:
            curr += char
    answer += curr[::-1]
    return answer


def reverseWordsFail(s: str) -> str:
    # word내에서 바꿔야함! word순서도 거꾸로 되어서 안됨!
    answer = ""
    for i in range(len(s) - 1, -1, -1):
        answer += s[i]
    return answer


def reverseWordsFail2(s: str) -> str:
    start = 0
    for i in range(len(s)):
        if s[i] == " ":
            for j in range(start, i):
                # str object does not support item assignment
                temp = s[j]
                s[j] = s[i - 1 - j]
                s[i - 1 - j] = temp
            start = i + 1

    return s


print(reverseWords2("Let's take LeetCode contest"))
print(reverseWords2("God Ding"))
