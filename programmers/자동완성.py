from typing import List


# 총 단어의 수 N, 각 단어의  최대 길이 L. O(N * L)
def solution(words: List[str]) -> int:
    root = {}
    flag = "Flag"
    root[flag] = True

    for word in words:
        curr = root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
            if not curr:
                curr[flag] = True
            else:
                curr[flag] = False

    print(root)

    total_count = 0
    for word in words:
        curr = root
        count = 0
        for c in word:
            count += 1
            curr = curr[c]
            if curr[flag]:
                break
        print(word, count)
        total_count += count
    return total_count


# 중복 없는 단어 N개.
print(solution(["go", "gone", "guild"]))
print(solution(["abc", "def", "ghi", "jklm"]))
print(solution(["word", "war", "warrior", "world"]))
