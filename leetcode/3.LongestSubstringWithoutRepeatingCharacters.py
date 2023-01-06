def longest_substring_without_repeating_characters(s: str) -> int:
    '''set 자료형 사용'''
    answer = 0
    for start in range(len(s)):
        temp = set()
        for end in range(start, len(s)):
            char = s[end]
            if char in temp:
                break
            temp.add(char)
            answer = max(answer, len(temp))
    return answer


def longest_substring_without_repeating_characters2(s: str) -> int:
    '''슬라이딩 윈도우와 투 포인터로 사이즈 조절'''

    # 문자별 가장 큰 인덱스
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)

        used[char] = index
    return max_length


print(longest_substring_without_repeating_characters2("abcabcbb"))
print(longest_substring_without_repeating_characters2("bbbbb"))
print(longest_substring_without_repeating_characters2("pwwkew"))
