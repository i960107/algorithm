from typing import List


def solution(n: int, words: List[str]) -> List[int]:
    answer = [0, 0]
    words_set = set()
    i = 0
    prev = None
    while i < len(words):
        curr = words[i]
        if len(curr) <= 1 or (prev and prev[-1] != curr[0]) or (curr in words_set):
            # 탈락하는 경우
            answer = [(i % n) + 1, i // n + 1]
            break
        else:
            words_set.add(curr)
            prev = curr
            i += 1

    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,
               ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
                "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
